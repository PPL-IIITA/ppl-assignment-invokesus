from driver import *
from generator import generate
from miser_boy import Miser_Boy
from geek_boy import Geek_Boy
from generous_boy import Generous_Boy

from choosy_girl import Choosy_Girl
from normal_girl import Normal_Girl
from desperate_girl import Desperate_Girl

import logging
import pickle

generate()
B = create_boys()
G = create_girls()

logging.info('Profile Matching start:\n')
for g in G:
    for b in B:
        logging.info('Commitment: Girl ' + g.name +' is checking profile of Boy '+b.name)
        if  check_eligibility(b, g):
            g.committed = True
            b.committed = True
            g.paired_to = b.name
            b.paired_to = g.name
            logging.info('Commitment Girl: '+g.name+' got commited with boy: '+b.name)
            couples.append((b,g))
            break

print("Couples formed \n")
for g in G:
    if g.committed == False:
        print('Girl: ' + g.name + '  is not commited to anyone')
    else:
        print('Girl: ' + g.name + '  is commited with  Boy: ' + g.paired_to)

pickle.dump(couples, open( "couples.p", "wb" ))
