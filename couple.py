
class Couple:
    """
    Has methods  happiness and compatibility
    """
    def __init__(self, boy, girl):
        self.boy = boy
        self.girl = girl
    def happiness(self):
        """
        The happiness of a couple is defined as the sum of the happiness of both girl and boy.
        """
        return (self.boy.happiness + self.girl.happiness()) 

    def compatibility(self):
        """
        The compatibility of a couple is defined as the sum of: magnitude by which the budget of the boy exceeds the maintenance cost of the girl, the absolute value of the difference in attractiveness, and the absolute value of the difference of intelligence.

        """
        return ((self.boy.budget - self.girl.maintenance) + abs(self.boy.attractiveness - self.girl.attractiveness) + abs (self.boy.intelligence - self.girl.intelligence) )
