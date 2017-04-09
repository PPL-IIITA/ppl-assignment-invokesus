from gift import Gift

class Utility_Gift(Gift):
    """
    Associated with the utility value, utility class, value and price.
    """
    def __init__ (self, price, value, utility_value, utility_class):
            super.__init__(price, value)
            self.utility_view = utility_value
            self.utility_class = utility_class
