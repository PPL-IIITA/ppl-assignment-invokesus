from gift import Gift

class Essential_Gift(Gift):
    """
    Bare minimal gifts and are associated with a price and value.
    """
    def __init__ (self, price, value):
            super.__init__(price, value)
