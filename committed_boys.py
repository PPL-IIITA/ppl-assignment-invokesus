import pickle

class Partner(object):

    """ Base class for the three implementations
    """

    def __init__(self, boy_name_list):

        self.boy_name_list = boy_name_list
        self.girl_name_list = []
        self.committedboys = []

    def generate_committed_boy_pool(self):
        '''GENERATES LIST OF COMMITTED BOYS'''
        couples_list = pickle.load(open("couple.p", "rb"))
        for couple in couples_list:
            self.committed_boy_pool.append(couple.boy)
