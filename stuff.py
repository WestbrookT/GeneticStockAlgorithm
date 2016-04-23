import sent
import stats
import stockBot as sb

#time.sleep(8500)
s = sent.Sentiment(sent.token, sent.secret_key)

def first(trades, sector, ticker):
    out = sector.earnings_yield_comparison(ticker)
    print("{}, EY: {}".format(ticker, out))
    return out

def sec(trades, sector, ticker):
    out =  s.twitter_sentiment(sector.sector_data[ticker])
    print("{}, T: {}".format(ticker, out))
    return out

def third(trades, sector, ticker):
    data = trades.last_trade(ticker)

    if data == 'No data':
        return 0
    if data[0] == 'buy':
        val = float(stats.ask(ticker))
        if val > data[2]:
            print('Change:')
            print(val/data[2]*-1)
            return val/data[2]*-1
        else:
            print('Change:')
            print(data[2]/val)
            return data[2]/val
    else:
        val = stats.ask(ticker)
        if val > data[2]:
            print('Change:')
            print(val/data[2]*-1)
            return val/data[2]*-1
        else:
            print('Change:')
            print(data[2]/val)
            return data[2]/val




bot = sb.GeneticBot([first, sec, third], 'tech', 'trades', 100)

#bot = sb.create_from_file('genbot.pickle')

bot.timescale = 1
bot.mutate_every_x  = 2

bot.run_x_iterations(6)


