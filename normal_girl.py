class Normal_Girl(object):
    """
    The choosy, whose happiness in a relationship is logarithmic of the total cost of gifts achieved over maintenance. However the luxury gifts are very previous and count double the normal value.
    """
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

