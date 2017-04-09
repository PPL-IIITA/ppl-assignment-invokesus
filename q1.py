from q1_helper import *
from miser_boy import Miser_Boy
from geek_boy import Geek_Boy
from generous_boy import Generous_Boy
from couple import Couple
from choosy_girl import Choosy_Girl
from normal_girl import Normal_Girl
from desperate_girl import Desperate_Girl

import logging
import pickle

B = create_boys()
G = create_girls()
couples = []
logging.basicConfig(format='%(asctime)s %(name)s -  %(message)s:',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='log.txt',filemode='w')

logging.info('Profile Matching start:\n')
for g in G:
    for b in B:
        if  check_eligibility(b, g):
            g.committed = True
            b.committed = True
            g.paired_to = b.name
            b.paired_to = g.name
            logging.info('Commitment :: Girl: '+g.name+' Boy: '+b.name)
            couples.append((b,g))
            break

print("Couples formed \n")
for g in G:
    if g.committed == False:
        print('Girl: ' + g.name + '  is not commited to anyone')
    else:
        print('Girl: ' + g.name + '  is commited with  Boy: ' + g.paired_to)

pickle.dump(couples, open( "couples_q1.p", "wb" ))
pickle.dump(B, open( "boys.p", "wb" ))
pickle.dump(G, open( "girls.p", "wb" ))
