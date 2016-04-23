


f = open('stats.py', 'w')

data = {
    'ask': 'a',
    'bid': 'b',
    'ask_realtime': 'b2',
    'bid_realtime': 'b3',
    'previous_close': 'p',
    'open': 'o',
    'dividend_yield': 'y',
    'dividend_per_share': 'd',
    'ex_dividend_date': 'q',
    'change': 'c1',
    'change_and_percent_change': 'c',
    'change_realtime': 'c6',
    'change_percent': 'k2',
    'change_in_percent': 'p2',
    'last_trade_date': 'd1',
    'trade_date': 'd2',
    'last_trade_time': 't1',
    'after_hours_change': 'c8',
    'commission': 'c3',
    'days_low': 'g',
    'days_high': 'h',
    'last_trade_realtime_with_time': 'k1',
    'last_trade_with_time': 'l',
    'last_trade_value': 'l1',
    'one_year_target_price': 't8',
    'year_high': 'k',
    'year_low': 'j',
    'year_range': 'w',
    'market_capitalization': 'j1',
    'name': 'n',
    'shares_outstanding': 'j2',
    'volume': 'v',
    'ask_size': 'a5',
    'bid_size': 'b6',
    'last_trade_size': 'k3',
    'earnings_per_share': 'e',
    'eps_est_year': 'e7',
    'pe_ratio': 'r2'
}

f.write('import requests, inspect, sys\n\n\n')

for func in data.keys():
    f.write('def {}(ticker):\n'.format(func))
    f.write("    r = requests.get('http://finance.yahoo.com/d/quotes.csv?s={}&f={}'.format(ticker))\n".format("{}", data[func]))
    f.write("    hold = r.text.rstrip().strip().split(',')\n")
    #f.write("    print(hold)\n")
    f.write("    try:\n")
    f.write("        return float(hold[0])\n")
    f.write("    except:\n")
    f.write("        return hold[0]\n\n\n")