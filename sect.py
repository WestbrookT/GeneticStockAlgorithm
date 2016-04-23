import requests, store, yaml


def earnings_yield(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=ae'.format(ticker))

    hold = r.text.rstrip().strip().split(',')

    EY = float(hold[1])/float(hold[0])
    return EY

def price(ticker):
    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f=a'.format(ticker))

    hold = r.text.rstrip().strip().split(',')


    return hold[0]

def get_sectors():
    with open('sectors.yaml', 'r') as f:
        data = yaml.safe_load(f)
        return data


def write_sectors(data):
    with open('sectors.yaml', 'w') as f:
        f.write(yaml.dump(data))



class Sector:



    def __init__(self, sect):
        if type(sect) == type({}):
            self.sector_data = sect
            return

        self.sector_data = get_sectors()[sect]




    def avg_sector_earnings_yield(self):
        total = 0.0
        count = 0

        for ticker in self.sector_data:

            total += earnings_yield(ticker)
            count += 1
        return total/count

    def earnings_yield_comparison(self, ticker):
        return earnings_yield(ticker)/self.avg_sector_earnings_yield()

    def get_custom_data(self, tickers, format):
        r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f={}'.format(str(tickers)[1:-1], format))

        hold = r.text.rstrip().strip().split(',')

        return list(hold)



