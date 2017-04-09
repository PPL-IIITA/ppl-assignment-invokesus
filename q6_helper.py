import logging
from couple import Couple
from q1_helper import check_eligibility




def newpartner(B, G, couples_list, t):
    """allocates new boys to the girls who broke up
    """
    print(couples_list)
    couples_list.sort(key=lambda x: x.happiness())
    R = []

    for couple in couples_list:
        if couple.happiness() < t:
            couple.boy.committed = False
            couple.boy.paired_to = ''
            couple.girl.committed = False
            couple.girl.paired_to = ''
            for temp,i in enumerate(B):
                if i.name == couple.boy.name:
                    B[temp].committed = False
                    B[temp].paired_to = False
                    break

            for temp,i in enumerate(G):
                if i.name == couple.girl.name:
                    G[temp].committed = False
                    G[temp].paired_to = False
                    break
            couples_list.remove(couple)
            R.append(couple)


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
                        couples_list.append((Couple(b,G[temp])))
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

def gifting(couples_list, gift_list):
    """
    Performs gifting operation by selecting gifts one by one from sorted list until maintenance of girl is met.
    """

    happy_couples_list = []
    for i in couples_list:
        b = i.boy
        g = i.girl
        j = 0
        while b.expenditure < g.maintenance:
            if (b.budget -b.expenditure - gift_list[j][2]) > 0 :
                b.expenditure += gift_list[j][2]
                g.giftworth(gift_list[j])
                j +=1
                logging.info('Gifting :: Boy: ' + b.name + ' gifted Girlfriend: ' + g.name + ' Gift: ' + gift_list[j][0] + 'Price: ' + str(gift_list[j][2]))
            else:
                break

        #Tries to buy one luxury gift with the rest of the budget if a Geek
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

        #Buys as many gifts as his budget allows
        if b.type == "Generous":
            while b.budget > 0:
                if (b.budget -b.expenditure - gift_list[j][2]) > 0 :
                    b.expenditure += gift_list[j][2]
                    g.giftworth(gift_list[j])
                    j +=1
                    logging.info('Gifting :: Boy: ' + b.name + ' gifted Girlfriend: ' + g.name + ' Gift: ' + gift_list[j][0] + 'Price: ' + str(gift_list[j][2]))
                else :
                    break

        #Case included in case maintenance of girl is not met. Then boy is forced to increase budget to buy one more gift
        if b.expenditure < g.maintenance:
            b.expenditure += gift_list[j][2]
            g.giftworth(gift_list[j])
            b.budget = b.expenditure
            j+=1
            logging.info('Gifting :: Boy: ' + b.name + ' gifted Girlfriend: ' + g.name + ' Gift: ' + gift_list[j][0] + 'Price: ' + str(gift_list[j][2]))

        #Create new instance of couple to append to couples_list
        C = Couple (b,g)
        happy_couples_list.append(C)
    return happy_couples_list
