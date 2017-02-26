from math import pow, e
class Desperate_Girl(object):
    """
    Happiness is exponential function of attribute gift_appreciation
    The desperate, whose happiness in a relationship is exponential to the total cost of gifts received over maintenance, including luxury gifts. The value is not considered.
    """
    def __init__(self, name, attractiveness, intelligence, maintenance, committed, paired_to):
        self.name = name
        self.attractiveness = attractiveness 
        self.intelligence = intelligence 
        self.maintenance = maintenance
        self.committed = committed
        self.paired_to = paired_to
        self.type = "Desperate"
        self.gift_appreciation = 0

    def giftworth (self, gift):
            self.gift_appreciation += gift[2] 

    def happiness (self):
        return (pow(1.001,(self.gift_appreciation)))

