import interface

class Coincheck(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'coincheck'

    def markets(self):
        return ['btc/jpy']

