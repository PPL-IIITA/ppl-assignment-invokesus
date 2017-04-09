from q1_helper import create_boys, create_girls
from q4_helper import newpartner
import pickle
from random import randint
boys_list = pickle.load( open( "boys.p", "r+b" ) )
girls_list = pickle.load( open( "girls.p", "r+b" ) )
couples_list = pickle.load( open( "couples.p", "r+b" ) )
k = randint(1, len(couples_list))

newpartner(boys_list, girls_list, couples_list, k)
