import logging
from couple import Couple
from q1_helper import check_eligibility

def newpartner(boys, girls, couples_list, t):
    """Allocates new boys to the girls who broke up
    """
    couples_list.sort(key=lambda x: x.happiness()) #Sorting by happiness of the couple
    broken_couples = []

    for couple in couples_list:
        if couple.happiness() < t:
            couple.boy.committed = False
            couple.boy.paired_to = ''
            couple.girl.committed = False
            couple.girl.paired_to = ''

            for temp,i in enumerate(boys):
                if i.name == couple.boy.name:
                    boys[temp].committed = False
                    boys[temp].paired_to = False
                    break

            for temp, i in enumerate(girls):
                if i.name == couple.girl.name:
                    girls[temp].committed = False
                    girls[temp].paired_to = False
                    break

            couples_list.remove(couple)
            broken_couples.append(couple)

    print ("\nStatus of Girls after Breakups: \n")

    for g in girls:
        if g.committed:
            print ("Girl: " + g.name + " is committed to Boy: " + g.paired_to)

        else:
            print ("Girl: " + g.name +  " is single")

    for broken_couple in broken_couples:
        for b in boys:
            logging.info("Commitment:  Girl: " + broken_couple.girl.name + " is checking out  Boy: " + b.name)

            if check_eligibility(b, broken_couple.girl) and (b.name != broken_couple.boy.name):
                b.committed = True
                b.paired_to = broken_couple.girl.name
                broken_couple.girl.committed = True
                for temp, i in enumerate(girls):
                    if i.name == broken_couple.girl.name:
                        girls[temp].committed = True
                        girls[temp].paired_to = b.name
                        couples_list.append((Couple(b,girls[temp])))
                        logging.info("Commitment:  Girl: " + broken_couple.girl.name + " got committed with  Boy: " + b.name)
                        break

            if broken_couple.girl.committed:
                break

    print ("\nStatus of Girls after Finding New Boyfriends:\n")

    for g in girls:
        if g.committed == False:
            print ('Girl: ' + g.name + '  is single')

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
