from find_partner import Find_Partner

class Find_Partner_List(Find_Partner):

    def __init__(self, names):
        super().__init__(names)

    def search(self, boy_name):
        for i in self.committed_boys:
            if i.name == boy_name:
                return (i.paired_to)
    def print_girlfriend(self):
        for  i in self.sample:
            x = self.search(i)
            if x:
                print(i + "is committed to " + x)
            else:
                print(i + "is single.")
