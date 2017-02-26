class Normal_Girl:
    def __init__(self, name, attractiveness, intelligence, maintenance, committed, paired_to):
        self.name = name
        self.attractiveness = attractiveness 
        self.intelligence = intelligence 
        self.maintenance = maintenance
        self.committed = committed
        self.paired_to = paired_to
        self.gift_appreciation = 0
        self.type = "Normal"

    def giftworth (self, gift):
        self.gift_appreciation += (gift[2] +gift[3]) 

    def happiness (self):
        return (self.gift_appreciation)

