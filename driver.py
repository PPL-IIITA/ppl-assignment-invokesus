from miser_boy import Miser_Boy
from geek_boy import Geek_Boy
from generous_boy import Generous_Boy

#from girls import Girl
#from utility import Utili

from choosy_girl import Choosy_Girl
from normal_girl import Normal_Girl
from desperate_girl import Desperate_Girl

import csv
import logging
import pickle

logging.basicConfig(format='%(asctime)s %(name)s - %(levelname)s %(message)s:',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='log.txt',filemode='w')

B = []
G = []
couples = []

def check_eligibility(boy, girl):
    if (boy.budget < girl.maintenance): 
        return False
    elif (boy.committed or girl.committed):
        return False
    else :
        return True

def sanitized_boy(row):
    arguments =[]
    arguments.append(row[0])
    arguments.append(int(row[1]))
    arguments.append(int(row[2]))
    arguments.append(int(row[3]))
    if row[4] == 'False':
        arguments.append(False)
    else:
        arguments.append(True) 
    arguments.append(int(row[5]))
    arguments.append(row[6])
    arguments.append(row[7])
    return arguments

def sanitized_girl(row):
    arguments =[]
    arguments.append(row[0])
    arguments.append(int(row[1]))
    arguments.append(int(row[2]))
    arguments.append(int(row[3]))
    if row[4] == 'False':
        arguments.append(False)
    else:
        arguments.append(True) 
    arguments.append(row[5])
    arguments.append(row[6])
    return arguments

def allocate():
    with open('boys.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            temp = 0
            arguments = sanitized_boy(row)
            if row[7] == "Miser":
                temp = Miser_Boy(*arguments[:-1])
            elif row[7] == "Geek":
                temp = Geek_Boy (*arguments[:-1])
            else :
                temp = Generous_Boy(*arguments[:-1])
            B.append(temp)
        csvfile.close()

    with open('girls.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            temp = 0
            arguments = sanitized_girl(row)
            if row[6] == "Choosy":
                temp = Choosy_Girl(*arguments[:-1])
            elif row[6] == "Normal":
                temp = Normal_Girl(*arguments[:-1])
            else :
                temp = Desperate_Girl(*arguments[:-1])
            G.append(temp)
        csvfile.close()

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
            #print (g)
            #print ([x for x in B if x.name==g.paired_to ])

allocate()
pickle.dump(couples, open( "couples.p", "wb" ))
