import logging
import random
from random import randint
from find_partner import Find_Partner
from find_partner_list import Find_Partner_List
from find_partner_hash import Find_Partner_Hash
from find_partner_sorted_list import Find_Partner_Sorted_List

from q1_helper import create_boys, create_girls

logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p',
        level=logging.DEBUG,
        filename='log.txt',
        filemode='w')


def allocate():

    B = []
    G = []
    B = create_boys()
    G = create_girls()

    boys_names = []
    for b in B:
        boys_names.append(b.name)
    k = randint(1, len(boys_names))
    sample = random.sample(boys_names, k)
    print ("Sample List of Boys: ")
    for boy in boys_names:
        print (boy)
    boy_partners = ''
    choice = int(input("Choose one of the 3 following implementations:\n1 - List\n2 - Sorted List\n3 - Hash table\n"))
    if choice == 1:
        boy_partners = Find_Partner_List(boys_names)
    elif choice == 2:
        boy_partners = Find_Partner_Sorted_List(boys_names)
        pass
    else:
        boy_partners = Find_Partner_Hash(boys_names)
        pass

    # boy_partners = (Find_Partner) boy_partners
    print ('\nGirlfriends for given boys:')
    boy_partners.print_girlfriend()

allocate()
