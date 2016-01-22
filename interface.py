import exceptions

class MarketExplorer:

    def exchange_name(self):
        """
        Get the name of this exchange
        @returns string
        """
        raise exceptions.NotImplementedError

    def markets(self):
        """
        get the markets
        @returns array of strings
        """
        raise exceptions.NotImplementedError

    def translate(self, stock):
        """
        translate the exchange-side stock to the tulip-bot stockname
        An exchange may override this. Rules must be exactly the same as in
        the C++.
        @returns string
        """
        return stock.lower()

    def create_market(self, stock1, stock2):
        """
        Create an market name by calling trasnlate on both parameters
        and pasting them together.
        @returns string
        """
        return self.translate(stock1) + '/' + self.translate(stock2)