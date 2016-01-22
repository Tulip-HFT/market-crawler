import interface

class Okcoincn(interface.MarketExplorer):
    def __init__(self):
        pass

    def exchange_name(self):
        return 'okcoincn'

    def markets(self):
        return ['btc/cny', 'ltc/cny']

