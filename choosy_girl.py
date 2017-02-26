from  math import log
class Choosy_Girl:
    def __init__(self, name, attractiveness, intelligence, maintenance, committed, paired_to):
        self.name = name
        self.attractiveness = attractiveness 
        self.intelligence = intelligence 
        self.maintenance = maintenance
        self.committed = committed
        self.paired_to = paired_to
        self.type = "Choosy"
        self.gift_appreciation = 0

    def giftworth (self, gift):
        if gift[1] == "Luxury":
            self.gift_appreciation += gift[2] *2
        else :
            self.gift_appreciation += gift[2] 

    def happiness (self):
        return (log(self.gift_appreciation))
