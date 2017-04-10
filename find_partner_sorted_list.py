from find_partner import Find_Partner

class Find_Partner_Sorted_List(Find_Partner):

    def __init__(self, names):
        super().__init__(names)

    def binary_search(self, boy_name):
        for boy_name in self.samples:
            low, high = 0, len(self.committed_boys) - 1
            while low <= high:
                mid = (high + low) // 2
                if self.committed_boys[mid].name == boy_name:
                    has_girlfriend = True
                    self.girl_name_list.append(self.committed_boy_pool[mid].partner.name)
                    break
                elif self.committed_boys[mid].name > boy_name:
                    high = mid - 1
                else:
                    low = mid + 1
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
