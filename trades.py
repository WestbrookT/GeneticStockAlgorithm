import yaml, os

class Trades:


    def __init__(self, file_name):
        if file_name in os.listdir(os.getcwd()):

            f = open(file_name, 'r')
            self.y = yaml.safe_load(f)
            f.close()
            if type(self.y) != type({}):
                self.y = {}
        else:
            self.y = {}
        self.file_name = file_name

    def trade(self, ticker, type, amount, price, write=True):

        if ticker not in self.y.keys():
            self.y[ticker] = []
        self.y[ticker].append([type, amount, price])

        if write:
            self.write()

    def net(self, ticker):
        net = 0
        net_stocks = 0
        last_price = 0
        try:
            for trade in self.y[ticker]:
                if trade[0] == 'buy':
                    net -= trade[1] * float(trade[2])
                    net_stocks += trade[1]
                elif trade[0] == 'sell':
                    net += trade[1] * float(trade[2])
                    net_stocks -= trade[1]
                last_price = trade[2]
            return {'profit': net, 'net stocks': net_stocks, 'net value': net_stocks * last_price}
        except:
            return 'No trade data'

    def write(self):
        f = open(self.file_name, 'w')
        yaml.dump(self.y, f)
        f.close()

    def last_trade(self, ticker):
        try:
            return self.y[ticker][-1]
        except:
            return 'No data'