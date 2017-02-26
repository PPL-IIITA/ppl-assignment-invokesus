from math import exp
class Desperate_Girl:
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
        return ((self.gift_appreciation))

