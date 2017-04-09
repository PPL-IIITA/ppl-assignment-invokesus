from miser_boy import Miser_Boy
from geek_boy import Geek_Boy
from generous_boy import Generous_Boy

from choosy_girl import Choosy_Girl
from normal_girl import Normal_Girl
from desperate_girl import Desperate_Girl

import csv
import logging
import pickle


B = []
G = []
couples = []

def check_eligibility(boy, girl):
    if (boy.budget < girl.maintenance) or (girl.attractiveness < boy.attraction_requirement) or boy.committed or girl.committed:
        return False
    else :
        return True

def sanitized_boy(row):
    arguments =[]
    arguments.append(row[0])
    arguments.append(int(row[1]))
    arguments.append(int(row[2]))
    arguments.append(int(row[3]))
    arguments.append(int(row[4]))
    if row[5] == 'False':
        arguments.append(False)
    else:
        arguments.append(True)
    arguments.append(int(row[6]))
    arguments.append(row[7])
    arguments.append(row[8])
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

def create_boys():
    B = []
    with open('boys.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            temp = 0
            arguments = sanitized_boy(row)
            if row[8] == "Miser":
                temp = Miser_Boy(*arguments[:-1])
            elif row[8] == "Geek":
                temp = Geek_Boy (*arguments[:-1])
            else :
                temp = Generous_Boy(*arguments[:-1])
            B.append(temp)
        csvfile.close()
    return B

def create_girls():
    G = []
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
    return G


def assign():
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
            print('Girl: ' + g.name + '  is not committed to anyone')
        else:
            print('Girl: ' + g.name + '  is committed with  Boy: ' + g.paired_to)

    pickle.dump(couples, open( "couples_q1.p", "wb" ))
    pickle.dump(B, open( "boys.p", "wb" ))
    pickle.dump(G, open( "girls.p", "wb" ))
    return couples
