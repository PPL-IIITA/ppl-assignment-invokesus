import q5_helper
from q1_helper import assign
from q2_helper import *


pairing_method = int(input("Enter 1 for method in q1 or 2 for method in q5:  "))

if pairing_method == 1:
    couples_list = assign()
    gift_list = gift_sort()

    final_couples_list = gifting(couples_list, gift_list)

    happy_couples_list = sort_by_happiness (final_couples_list)
    print ("The value of k is a random integer and in this case it is " +(str(len(happy_couples_list))))
    print (str(len(happy_couples_list)) + " happiest couples are:")
    for i in happy_couples_list:
        print ("Boy: " + i.boy.name + " Girl: " + i.girl.name + " Happiness: " + str(i.happiness()))


elif pairing_method == 2:
    q5_helper.allocate()
else:
    print("Wrong option")
