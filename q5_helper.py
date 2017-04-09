from q1_helper import check_eligibility, create_boys, create_girls
import logging
from q2_helper import *



def allocate():
    'reads and stores the input from the boys.csv and girls.csv files and then makes the valid couples'
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
    					datefmt='%d/%m/%Y %I:%M:%S %p',
    					level=logging.DEBUG,
                        filename='log.txt',
                        filemode='w')
    couples_list = []
    B = create_boys()
    G = create_girls()

    B1 = sorted(B, key=lambda item: item.attractiveness, reverse=True)
    B2 = sorted(B, key=lambda item: item.attractiveness, reverse=True)
    G1 = sorted(G, key=lambda item: item.maintenance, reverse=True)
    SG = sorted(G, key=lambda item: item.attractiveness, reverse=True)

    logging.warning('Check-out session going on ahead:\n')
    for i in range(5):
        if (i % 2 == 0):
            for g in G1:
                if (g.committed == False):
                    break
            for b in B1:
                logging.info('Commitment:  Girl: ' + g.name + '  is checking out  Boy: ' + b.name)
                if check_eligibility(b,g):
                    b.committed = True
                    g.committed = True
                    g.paired_to = b.name
                    b.paired_to = g.name
                    logging.info('Commitment:  Girl: ' + g.name + '  got committed with  Boy: ' + b.name)
                    couples_list.append((b,g))
                    break
            G1.remove(g)
        else:
            for b in B2:
                if (b.committed == False):
                    break
            for g in SG:
                logging.info('Commitment:  Boy: ' + b.name + '  is checking out  Girl: ' + g.name)
                if check_eligibility(b,g):
                    b.committed = True
                    g.committed = True
                    g.paired_to = b.name
                    b.paired_to = g.name
                    logging.info('Commitment:  Boy: ' + b.name + '  got committed with  Girl: ' + g.name)
                    couples_list.append((b,g))
                    break
            B2.remove(b)

    print ('Couples formed (using new mechanism given in question 5):\n')
    for g in G:
        if g.committed == False:
            print ('Girl: ' + g.name + '  is not committed to anyone')
        else:
            print ('Girl: ' + g.name + '  is committed with  Boy: ' + g.paired_to)

    print ('\n')
    gift_list = gift_sort()

    final_couples_list = gifting(couples_list, gift_list)

    happy_couples_list = sort_by_happiness (final_couples_list)
    print ("The value of k is a random integer and in this case it is " +(str(len(happy_couples_list))))
    print (str(len(happy_couples_list)) + " happiest couples are:")
    for i in happy_couples_list:
        print ("Boy: " + i.boy.name + " Girl: " + i.girl.name + " Happiness: " + str(i.happiness()))
