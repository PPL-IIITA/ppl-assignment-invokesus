import csv
import pickle
from couple import Couple

couples_list = pickle.load( open( "couples.p", "rb" ) )
happy_couples_list = []
compatible_couples_list=[]
def gift_sort():
    with open('gifts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        temp = [row for row in reader]
        csvfile.close()
        temp = [[x[0], x[1], int(x[2]), int(x[3])] for x in temp]
        temp = (sorted(temp, key=lambda gift: gift[2]))
        return temp

gift_list = gift_sort()
for i in couples_list:
    b = i[0]
    g = i[1]
    j = 0
    while b.expenditure < g.maintenance:
        if (b.budget - gift_list[j][2]) > 0 :
            b.expenditure += gift_list[j][2]
            g.giftworth(gift_list[j])
            j +=1

    if b.type == "Geek":
        while (j < 1000): 
            if gift_list[j][1] == "Luxury":
                if (b.budget - gift_list[j][2] > 0 ):
                    b.expenditure += gift_list[j][2]
                    g.giftworth(gift_list[j])
                else :
                    break
            j +=1

    if b.type == "Generous":
        while b.budget > 0:
            if (b.budget - gift_list[j][2]) > 0 :
                b.expenditure += gift_list[j][2]
                g.giftworth(gift_list[j])
                j +=1
            else :
                break
    C = Couple (b,g)
    happy_couples_list.append(C)
happy_couples_list = sorted(happy_couples_list, key = lambda x: x.happiness())
happy_couples_list.reverse()
for i in happy_couples_list:
    print (i.happiness())
compatible_couples_list = sorted(happy_couples_list, key = lambda x: x.compatibility())
compatible_couples_list.reverse()
print()
for i in compatible_couples_list:
    print (i.compatibility())
