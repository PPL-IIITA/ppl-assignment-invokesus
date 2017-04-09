from q1_helper import check_eligibility, create_boys, create_girls
import logging
from q2_helper import *
from copy import deepcopy
from random import randint

def allocate():
    couples_list = []
    B = create_boys()
    G = create_girls()
    boys_list_copy_1 = sorted(B, key=lambda x: x.attractiveness, reverse=True)
    boys_list_copy_2 = deepcopy(boys_list_copy_1)
    logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    level=logging.DEBUG,
                    filename='log.txt',
                    filemode='w')

    girls_list_copy_1 = sorted(G, key=lambda x: x.maintenance, reverse=True)
    sorted_girls = sorted(G, key=lambda x: x.attractiveness, reverse=True)

    logging.warning('Couples Tryouts Taking Place:\n')
    print(len(G))
    l = randint(1, len(G) - 1)

    for i in range(l):
        if (i % 2 == 0):
            for g in girls_list_copy_1:
                if (g.committed == False):
                    break

            for b in boys_list_copy_1:
                logging.info('Commitment:  Girl: ' + g.name + '  is checking out  Boy: ' + b.name)

                if check_eligibility(b,g):
                    b.committed = True
                    g.committed = True
                    g.paired_to = b.name
                    b.paired_to = g.name
                    logging.info('Commitment:  Girl: ' + g.name + '  got committed with  Boy: ' + b.name)
                    couples_list.append((b,g))
                    break

            girls_list_copy_1.remove(g)

        else:
            for b in boys_list_copy_2:
                if (b.committed == False):
                    break

            for g in sorted_girls:
                logging.info('Commitment:  Boy: ' + b.name + '  is checking out  Girl: ' + g.name)
                if check_eligibility(b,g):
                    b.committed = True
                    g.committed = True
                    g.paired_to = b.name
                    b.paired_to = g.name
                    logging.info('Commitment:  Boy: ' + b.name + '  got committed with  Girl: ' + g.name)
                    couples_list.append((b,g))
                    break

            boys_list_copy_2.remove(b)

    print ('\nCouples formed using Algorithm of Question 5:\n')
    for g in G:
        if g.committed == False:
            print ('Girl: ' + g.name + '  is single')
        else:
            print ('Girl: ' + g.name + '  is committed with  Boy: ' + g.paired_to)

    gift_list = gift_sort()
    final_couples_list = gifting(couples_list, gift_list)
    happy_couples_list = sort_by_happiness (final_couples_list)
    print ("\nThe value of k is a random integer and in this case it is " +(str(len(happy_couples_list))))
    print (str(len(happy_couples_list)) + " happiest couples are:")

    for i in happy_couples_list:
        print ("Boy: " + i.boy.name + " Girl: " + i.girl.name + " Happiness: " + str(i.happiness()))
