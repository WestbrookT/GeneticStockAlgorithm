import sent, sect, store

# Equation = w(ey/aey) + w(TS) + w(PL)


class Bot:

    # values should be a list of tuples with a weight and a value, value can be numerical or a function: (weight, value)
    # if it is a function, you should be able to pass the bot itself and a ticker,
    # so that all information the bot has is available
    def __init__(self, values, sector):
        self.terms = values
        self.sector = sector

    def trade_suggestions(self):
        suggestions = {
            'buy': [],
            'sell': []
        }

        for ticker in self.sector.keys():




    def company_value(self, ticker):
        total = 0
        for v in self.terms:
            if callable(v[1]):
                total += v[1](self.sector, ticker)*v[0]
            else:
                total += v[0]*v[1]
        return total

    def make_trades(self):
        pass




class GeneticBot(Bot):

    # Values should be a list of functions or numerical values that are used to determine buy/sell/hold
    # these values will be assigned weights by this class
    def __int__(self, terms):
        pass