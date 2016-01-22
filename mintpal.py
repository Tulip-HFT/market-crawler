import urllib2
import json

import interface

class Mintpal(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'mintpal'

    def markets(self):
        req = urllib2.urlopen('https://api.mintpal.com/v2/market/summary/')
        js = json.loads(req.read())
        # TODO: parse when the api works again.
        raise NotImplementedError
