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
    if (boy.budget < girl.maintenance) or boy.committed or girl.committed: 
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

def create_boys():
    B = []
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
