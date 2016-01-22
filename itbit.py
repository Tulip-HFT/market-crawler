import interface

class Itbit(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'itbit'

    def markets(self):
        return ['btc/usd', 'btc/sgd', 'btc/eur']

