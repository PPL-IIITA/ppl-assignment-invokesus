from gift import Gift

class Luxury_Gift(Gift):
    """
    Attributes of the luxury rating, difficulty to obtain the gift, value and price.
    """
    def __init__ (self, price, value, luxury_rating, difficulty_to_obtain):
            super.__init__(price, value)
            self.luxury_rating = luxury_rating
            self.difficulty_to_obtain = difficulty_to_obtain
