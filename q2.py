def define(self, symbol, value):
        """Define Scheme SYMBOL to have VALUE."""
        # BEGIN PROBLEM 2
        self.bindings[symbol]=value
        
        # END PROBLEM 2

    def lookup(self, symbol):
        """Return the value bound to SYMBOL. Errors if SYMBOL is not found."""
        # BEGIN PROBLEM 2

        if symbol in self.bindings:
            return self.bindings[symbol]
        elif self.parent:

            return self.parent.lookup(symbol)
        
        # END PROBLEM 2
        raise SchemeError('unknown identifier: {0}'.format(symbol))


