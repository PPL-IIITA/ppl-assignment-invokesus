from find_partner import Find_Partner

class Find_Partner_Hash(Find_Partner):

    def __init__(self, names):
        super().__init__(names)

    def generate_boy_hash(self):
        super(PartnerHash, self).generate_committed_boys()
        for boy in self.committed_boys:
            self.boy_hash[boy.name] = boy.partner.name
    def get_girlfriend_name_hash_table(self):
        self.generate_boy_hash()
        for boy_name in self.sample:
            if boy_name in self.boy_hash:
                pass
        return self.girl_name_list
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
