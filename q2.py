import pickle
from couple import Couple
from q2_helper import *

couples_list = pickle.load( open( "couples.p", "rb" ) )
gift_list = gift_sort()

final_couples_list = gifting(couples_list, gift_list)

happy_couples_list = sort_by_happiness (final_couples_list)
compatible_couples_list = sort_by_compatibility (final_couples_list)

for i in happy_couples_list:
    print ("Boy: " + i.boy.name + " Girl: " + i.girl.name + " Happiness: " + str(i.happiness()))
print ()
for i in compatible_couples_list:
    print ("Boy: " + i.boy.name + " Girl: " + i.girl.name + " Compatibility: " + str(i.compatibility()))
