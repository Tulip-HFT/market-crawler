import interface

import urllib2
import re

class Cexio(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'cex'

    def markets(self):
        return ['btc/usd']
        # NOTE: currently we have not implemented other markets than BTC/USD
        # in CEX.IO. this is because CEX offers an awfull api to query open
        # orders, and i don't belive anyone is going to use it anyway.
        # you can uncomment the above line to make all CEX markets available
        # in the ui. Just remember that they don't actually work... If you 
        # miss them, create a feature request ;).
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')] # silly API.
        req = opener.open('https://cex.io/')
        html = req.read()
        markets = []
        for pri, sec in re.findall(r'href="#([A-Z]+)-([A-Z]+)"', html):
            markets.append(self.create_market(pri, sec))

        return list(set(markets))
