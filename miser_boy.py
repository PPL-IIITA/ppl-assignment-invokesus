from boy import Boy

class Miser_Boy(Boy):
    def __init__(self, name, attractiveness, intelligence, budget, attraction_requirement, committed, expenditure, paired_to):
        super().__init__(name, attractiveness, intelligence, budget, attraction_requirement, committed, expenditure, paired_to)
        self.type = "Miser"

    def happiness(self, *args):
        self.happiness =(self.budget - self.expenditure)
        return (self.budget - self.expenditure)
