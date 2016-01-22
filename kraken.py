import urllib2
import json

import interface

class Kraken(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'kraken'

    def markets(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')] # silly API.
        req = opener.open('https://api.kraken.com/0/public/AssetPairs')
        js = json.loads(req.read())
        markets = []
        for k, v in js['result'].items():
            markets.append(self.create_market(v['base'], v['quote']))
        return markets

    def translate(self, stock):
        stock = stock[1:].lower()
        if stock == 'xbt': stock = 'btc'
        if stock == 'xdg': stock = 'doge'
        return stock