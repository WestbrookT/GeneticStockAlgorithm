import requests, inspect, sys


def ask(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=a'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def previous_close(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=p'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def change(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=c1'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def last_trade_time(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=t1'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def eps_est_year(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=e7'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def open(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=o'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def dividend_yield(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=y'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def one_year_target_price(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=t8'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def ex_dividend_date(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=q'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def commission(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=c3'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def trade_date(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=d2'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def shares_outstanding(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=j2'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def ask_size(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=a5'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def ask_realtime(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=b2'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def change_and_percent_change(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=c'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def last_trade_with_time(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=l'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def bid(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=b'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def earnings_per_share(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=e'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def change_in_percent(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=p2'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def change_realtime(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=c6'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def last_trade_date(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=d1'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def dividend_per_share(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=d'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def year_range(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=w'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def after_hours_change(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=c8'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def volume(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=v'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def bid_size(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=b6'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def pe_ratio(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=r2'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def days_low(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=g'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def last_trade_value(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=l1'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def last_trade_size(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=k3'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def name(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=n'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def year_high(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=k'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def bid_realtime(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=b3'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def days_high(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=h'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def last_trade_realtime_with_time(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=k1'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def change_percent(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=k2'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def market_capitalization(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=j1'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def year_low(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=j'.format(ticker))
    hold = r.text.rstrip().strip().split(',')
    try:
        return float(hold[0])
    except:
        return hold[0]


def earnings_yield(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=ae'.format(ticker))

    hold = r.text.rstrip().strip().split(',')

    ey = float(hold[1])/float(hold[0])
    return ey


if __name__ == '__main__':
    allf = inspect.getmembers(sys.modules[__name__], inspect.isfunction)


    for i in allf:
        print(i)
        i[1]('GOOG')