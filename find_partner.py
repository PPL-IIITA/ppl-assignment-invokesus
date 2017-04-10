import pickle
class Find_Partner:
    def __init__(self, names):
        self.sample = names
        couples_list = pickle.load(open("couples.p", "rb"))
        self.committed_boys = [x.boy for x in couples_list]

    def print_girlfriend(self):
        for i in self.sample:
            print(self.search(i))

    def search(self, i):
        pass
