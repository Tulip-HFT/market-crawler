import urllib2
import json

import interface

class Cryptsy(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'cryptsy'

    def markets(self):
        req = urllib2.urlopen('http://pubapi.cryptsy.com/api.php?method=marketdatav2')
        # silly API: an 11MB request just to get the available markets...
        js = json.loads(req.read())
        markets = []
        for pair in js['return']['markets'].keys():
            pair = pair.partition('/')
            markets.append(self.create_market(pair[0], pair[2]))
        return markets

