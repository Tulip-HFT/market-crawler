import urllib2
import json

import interface

class Bitfinex(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'bitfinex'

    def markets(self):
        req = urllib2.urlopen('https://api.bitfinex.com/v1/symbols')
        js = json.loads(req.read())
        markets = []
        for pair in js:
            markets.append(self.create_market(pair[:3], pair[3:]))
            print pair
        return markets
 
