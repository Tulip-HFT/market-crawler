import urllib2
import json

import interface

class Hitbtc(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'hitbtc'

    def markets(self):
        req = urllib2.urlopen('https://api.hitbtc.com/api/1/public/symbols')
        js = json.loads(req.read())
        markets = [
            self.create_market(item['commodity'], item['currency'])
            for item in js['symbols']
        ]
        return markets
