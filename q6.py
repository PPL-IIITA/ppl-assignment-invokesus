import pickle
from couple import Couple
from q2_helper import gift_sort
from random import randint
import random
from q6_helper import *

temp_couples_list = pickle.load( open( "couples_q1.p", "rb" ) )
gift_list = gift_sort()
t = randint(1, len(temp_couples_list))
boys_list = pickle.load( open( "boys.p", "r+b" ) )
girls_list = pickle.load( open( "girls.p", "r+b" ) )


couples_list = [Couple(x[0], x[1]) for x in temp_couples_list]
print (couples_list)
for i in range(t):
    gifting(couples_list, gift_list)
    # print(1, couples_list)
    newpartner(boys_list, girls_list, couples_list, t)
    # print (couples_list)
