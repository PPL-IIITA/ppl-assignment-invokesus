import math

class Couple:
    def __init__(self, boy, girl):
        self.boy = boy
        self.girl = girl
    def happiness(self):
        return (self.boy.happiness + self.girl.happiness()) 

    def compatibility(self):
        return ((self.boy.budget - self.girl.maintenance) + abs(self.boy.attractiveness - self.girl.attractiveness) + abs (self.boy.intelligence - self.girl.intelligence) )
