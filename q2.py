import pickle
from couple import Couple
from q2driver import *

couples_list = pickle.load( open( "couples.p", "rb" ) )
gift_list = gift_sort()

final_couples_list = gifting(couples_list, gift_list)
happy_couples_list = sort_by_happiness (final_couples_list)
compatible_couples_list = sort_by_compatibility (final_couples_list)

for i in happy_couples_list:
    print (i.happiness())

for i in compatible_couples_list:
    print (i.compatibility())
