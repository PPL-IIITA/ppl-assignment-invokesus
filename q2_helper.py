import csv
from couple import Couple
import logging

logging.basicConfig(format='%(asctime)s %(name)s -  %(message)s:',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG,filename='log.txt',filemode='a')
def gift_sort():
    with open('gifts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        temp = [row for row in reader]
        csvfile.close()
        temp = [[x[0], x[1], int(x[2]), int(x[3])] for x in temp]
        temp = (sorted(temp, key=lambda gift: gift[2]))
        return temp

def gifting(couples_list, gift_list):
    happy_couples_list = []
    for i in couples_list:
        b = i[0]
        g = i[1]
        j = 0
        while b.expenditure < g.maintenance:
            if (b.budget -b.expenditure - gift_list[j][2]) > 0 :
                b.expenditure += gift_list[j][2]
                g.giftworth(gift_list[j])
                j +=1
                logging.info('Gifting :: Boy: ' + b.name + ' gifted Girlfriend: ' + g.name + ' Gift: ' + gift_list[j][0] + 'Price: ' + str(gift_list[j][2]))
            else:
                break

        if b.type == "Geek":
            while (j < 1000): 
                if gift_list[j][1] == "Luxury":
                    if (b.budget -b.expenditure - gift_list[j][2] > 0 ):
                        b.expenditure += gift_list[j][2]
                        g.giftworth(gift_list[j])
                        logging.info('Gifting :: Boy: ' + b.name + ' gifted Girlfriend: ' + g.name + ' Gift: ' + gift_list[j][0] + 'Price: ' + str(gift_list[j][2]))
                    else :
                        break
                j +=1

        if b.type == "Generous":
            while b.budget > 0:
                if (b.budget -b.expenditure - gift_list[j][2]) > 0 :
                    b.expenditure += gift_list[j][2]
                    g.giftworth(gift_list[j])
                    j +=1
                    logging.info('Gifting :: Boy: ' + b.name + ' gifted Girlfriend: ' + g.name + ' Gift: ' + gift_list[j][0] + 'Price: ' + str(gift_list[j][2]))
                else :
                    break
        C = Couple (b,g)
        happy_couples_list.append(C)
    return happy_couples_list

def sort_by_happiness (couples_list):
    couples_list = sorted(couples_list, key = lambda x: x.happiness())
    couples_list.reverse()
    return couples_list

def sort_by_compatibility (couples_list):
    couples_list = sorted(couples_list, key = lambda x: x.compatibility())
    couples_list.reverse()
    return couples_list
