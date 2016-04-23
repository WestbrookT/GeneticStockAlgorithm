import sect, trades
import bisect, yaml, time, random, pickle
# Equation = w(ey/aey) + w(TS) + w(PL)


class Bot:

    suggestions = {}
    top = 2
    bottom = 1


    # values should be a list of tuples with a weight and a value, value can be numerical or a function: (weight, value)
    # if it is a function, you should be able to pass the bot itself and a ticker,
    # so that all information the bot has is available
    def __init__(self, values, sector, trades_file, amount):
        self.terms = values
        self.sector = sect.Sector(sect.get_sectors()[sector])
        self.trades = trades.Trades(trades_file)


    def trade_suggestions(self):
        suggestions = {
            'buy': [],
            'sell': []
        }

        for ticker in self.sector.sector_data.keys():
            value = self.company_value(ticker)
            if value >= self.top:
                bisect.insort(suggestions['buy'], ticker)
            elif value <= self.bottom:
                bisect.insort(suggestions['sell'], ticker)

        self.suggestions = suggestions



    def company_value(self, ticker):
        total = 0
        for v in self.terms:
            if callable(v[1]):
                total += v[1](self.trades, self.sector, ticker)*v[0]
            else:
                total += v[0]*v[1]
        return total

    def make_trades(self, amount):

        for ticker in self.suggestions['buy']:
            price = float(sect.price(ticker))
            if callable(amount):
                self.trades.trade(ticker,'buy', amount(ticker), price)
            else:
                self.trades.trade(ticker, 'buy', amount, price)
        for ticker in self.suggestions['sell']:
            price = float(sect.price(ticker))
            if callable(amount):
                self.trades.trade(ticker,'sell', amount(ticker), price)
            else:
                self.trades.trade(ticker, 'sell', amount, price)





class GeneticBot:

    bots = []


    #timescale is how long between bot runs in seconds
    timescale = 600
    mutate_rate = .5
    mutate_scale = .1
    mutate_every_x = 4

    archive_file = 'archive.yaml'


    # terms should be a list of functions or numerical values that are used to determine buy/sell/hold
    # these values will be assigned weights by this class
    # sector is the string name of a defined sector
    def __init__(self, terms, sector, trades_file, amount):

        self.terms = terms
        self.sector_name = sector
        self.trades_file = trades_file
        self.amount = amount

    def archive(self):
        for bot in self.bots:
            print('here')
            with open(self.archive_file, 'a') as f:
                for i in range(0, 4):
                    with open('{}{}.yaml'.format(self.trades_file, i), 'r') as r:
                        transactions = yaml.safe_load(r)
                        out = {str(list(bot.terms)): transactions}
                        print(str(out))
                        yaml.dump(out, f)



    def mutate(self):
        bots = []
        top = 0
        bottom = 0
        bot = self.best(self.bots)
        self.archive()
        for botid in range(1, 5):
            terms = []
            for i in bot.terms:
                if (random.random() < self.mutate_rate):
                    sign = random.randint(0, 1)
                    signs = [1, -1]
                    sign = signs[sign]

                    new_weight = i[0]+sign*self.mutate_scale*i[0]
                    print(new_weight)

                    terms.append((new_weight, i[1]))
                else:
                    terms.append((1, i[1]))

                if random.random() < self.mutate_rate:
                    sign = random.randint(0, 1)
                    signs = [1, -1]
                    sign = signs[sign]
                    top = bot.top+sign*self.mutate_scale*bot.top

                if random.random() < self.mutate_rate:
                    sign = random.randint(0, 1)
                    signs = [1, -1]
                    sign = signs[sign]
                    bottom = bot.bottom+sign*self.mutate_scale*bot.bottom

            new_bot = Bot(terms, self.sector_name, "{}{}.yaml".format(self.trades_file, botid), self.amount)
            print('TERMS:')
            print(terms)
            print(bot.terms)
            new_bot.top = top
            new_bot.bottom = bottom
            bots.append(new_bot)
        bots.append(bot)
        print('.' + str(len(bots)))

        for i in range(0, 4):
            f = open('{}{}.yaml'.format(self.trades_file, i), 'w')
            f.write('')
            f.close()
        return bots


    def best(self, bots):
        top = 0
        top_index = 0
        for x in range(0, 4):

            val = 0
            for company in bots[x].sector.sector_data.keys():

                params = bots[x].trades.net(company)

                if params != 'No trade data':
                    val += params['net value'] + params['profit']
                else:
                    pass
            if val > top:
                top_index = x
                top = val

        return bots[top_index]



    def run_iteration(self):
        if len(self.bots) == 0:
            for x in range(0, 4):

                values = [(1, func) for func in self.terms]

                self.bots.append(Bot(values, self.sector_name, "{}{}.yaml".format(self.trades_file, x), self.amount))



        for bot in self.bots:
            bot.trade_suggestions()
            bot.make_trades(self.amount)



        print('..')



    def run_x_iterations(self, x):

        iteration = 0
        while iteration < x:

            self.run_iteration()
            self.store_current()

            if iteration % self.mutate_every_x == 1:
                self.mutate()

            iteration += 1
            if iteration == x:
                break
            its = 0

            best = self.best(self.bots)
            for ticker in best.sector.sector_data.keys():
                print(best.trades.net(ticker))

            while its < self.timescale:
                time.sleep(self.timescale/10)
                its += self.timescale/10
                print(its)

        best = self.best(self.bots)
        for ticker in best.sector.sector_data.keys():
            print(best.trades.net(ticker))



    def store_current(self):
        pickle.dump(self, open('genbot.pickle', 'wb'))



def create_from_file(file_name):
    return pickle.load(open(file_name, 'rb'))