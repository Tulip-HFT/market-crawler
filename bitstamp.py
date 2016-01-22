import interface

class Bitstamp(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'bitstamp'

    def markets(self):
        return ['btc/usd']

