import interface

class Okcoincom(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'okcoincom'

    def markets(self):
        return ['btc/usd', 'ltc/usd']

