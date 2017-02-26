import csv
import pickle
from couple import Couple

couples_list = pickle.load( open( "couples.p", "rb" ) )

def gift_sort():
    with open('gifts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        temp = [row for row in reader]
        csvfile.close()
        temp = [[x[:2], int(x[2]), int(x[3])] for x in temp]
        temp = (sorted(temp, key=lambda gift: gift[2]))
        return temp
gift_list = gift_sort()

for i in couples_list:
    b = i[0]
    g = i[1]
    while b.expenditure < g.maintenance:
        if (b.budget - giftlist[2]) > 0 :
            b.budget
