import urllib2
import json

import interface

class Poloniex(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'poloniex'

    def markets(self):
        req = urllib2.urlopen('https://poloniex.com/public?command=returnTicker')
        js = json.loads(req.read())
        markets = []
        for pair, value in js.iteritems():
            if value['isFrozen'] == "0":
                pairarr = pair.split('_')
                markets.append(self.create_market(pairarr[1], pairarr[0]))
            print pair
        return markets
 
