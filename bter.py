import urllib2
import json

import interface

class Bter(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'bter'

    def markets(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')] # silly API.
        req = opener.open('http://data.bter.com/api/1/marketlist')
        js = json.loads(req.read())
        markets = []
        for obj in js['data']:
            market_str = obj['pair']
            # bter logic: vol_a = float, vol_b = str
            vol = obj['vol_a'] + float(obj['vol_b'].replace(',', '.'))
            # only add the market if it has nonzero volume. I don't know exactly what
            # vol_a and vol_b are, but it seems to work.
            if vol:
                market = market_str.partition('_')
                markets.append(self.create_market(market[0], market[2]))

        return markets

