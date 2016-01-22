import urllib2
import json

import interface

class Btce(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'btce'

    def markets(self):
        req = urllib2.urlopen('https://btc-e.com/api/3/info')
        js = json.loads(req.read())
        markets = []
        for pair in js['pairs'].keys():
            a, _, b = pair.partition('_')
            markets.append(self.create_market(a, b))
        return markets

