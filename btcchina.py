import urllib2
import json

import interface

class Btcchina(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'btcchina'

    def markets(self):
        req = urllib2.urlopen('https://data.btcchina.com/data/ticker?market=all')
        js = json.loads(req.read())
        markets = []
        for key in js.keys():
            market = key.partition('_')[2]
            assert(len(market) == 6)
            markets.append(self.create_market(market[0:3], market[3:6]))
        return markets
