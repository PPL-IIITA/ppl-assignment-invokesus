from girl import Girl
from math import pow, e
class Desperate_Girl(Girl):
    """
    Happiness is exponential function of attribute gift_appreciation
    The desperate, whose happiness in a relationship is exponential to the total cost of gifts received over maintenance, including luxury gifts. The value is not considered.
    """
    def __init__(self, name, attractiveness, intelligence, maintenance, committed, paired_to):
        super().__init__(name, attractiveness, intelligence, maintenance, committed, paired_to)
        self.type = "Desperate"

    def giftworth (self, gift):
        self.gift_appreciation += gift[2]

    def happiness (self):
        return (pow(1.001,(self.gift_appreciation)))
