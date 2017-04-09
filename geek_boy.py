from boy import Boy

class Geek_Boy(Boy):
    def __init__(self, name, attractiveness, intelligence, budget, attraction_requirement, committed, expenditure, paired_to):
        super().__init__(name, attractiveness, intelligence, budget, attraction_requirement, committed, expenditure, paired_to)
        self.type = "Geek"

    def happiness(self, g):
        self.happiness = g.intelligence
        return (g.intelligence)
