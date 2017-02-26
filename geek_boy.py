class Geek_Boy:
    def __init__(self, name, attractiveness, intelligence, budget, committed, expenditure, paired_to):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.budget = budget
        self.committed = committed
        self.expenditure = expenditure 
        self.paired_to = paired_to
        self.happiness = 0
        self.type = "Geek"

    def happiness(self, g):
        self.happiness = g.intelligence
        return (g.intelligence)


