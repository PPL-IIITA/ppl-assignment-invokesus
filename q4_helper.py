import logging
from math import log
from q1_helper import check_eligibility
from couple import Couple

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.DEBUG,
                    filename='log.txt',
                    filemode='w')

def newpartner(B, G, couples_list, k):
    """allocates new boys to the girls who broke up
    """
    couples_list.sort(key=lambda x: x.happiness())
    R = []

    for couple in couples_list[:k]:
            couple.boy.committed = False
            couple.boy.paired_to = ''
            couple.boy.happiness = 0
            couple.girl.committed = False
            couple.girl.paired_to = ''
            couple.girl.happiness = 0
            for temp,i in enumerate(B):
                if i.name == couple.boy.name:
                    B[temp].committed = False
                    B[temp].paired_to = False
                    B[temp].happiness = 0
                    break

            for temp,i in enumerate(G):
                if i.name == couple.girl.name:
                    G[temp].committed = False
                    G[temp].paired_to = False
                    G[temp].happiness = 0
                    break

            R.append(couple)
    couples_list = couples_list[k:]


    print ('\nRemaining couples after Valentines Day(i.e. after breakups):\n')

    for g in G:
        if g.committed == False:
            print ('Girl: ' + g.name + '  is not committed to anyone')
        else:
            print ('Girl: ' + g.name + '  is committed with  Boy: ' + g.paired_to)

    logging.warning('Heart-broken Girls are checking out new boys ahead:\n')

    for broken_couple in R:
        for b in B:
            logging.info('Commitment:  Girl: ' + broken_couple.girl.name + '  is checking out  Boy: ' + b.name)
            if check_eligibility(b, broken_couple.girl) and (b.name != broken_couple.boy.name):
                b.committed = True
                b.paired_to = broken_couple.girl.name
                broken_couple.girl.committed = True
                for temp,i in enumerate(G):
                    if i.name == broken_couple.girl.name:
                        G[temp].committed = True
                        G[temp].paired_to = b.name
                        couples_list.append(Couple(b,G[temp]))
                        logging.info('Commitment:  Girl: ' + broken_couple.girl.name + '  got committed with  Boy: ' + b.name)
                        break
            if broken_couple.girl.committed:
                break

    print ('\nCouples after breakups:\n')
    for g in G:
        if g.committed == False:
            print ('Girl: ' + g.name + '  is not committed to anyone')
        else:
            print ('Girl: ' + g.name + '  is committed with  Boy: ' + g.paired_to)
