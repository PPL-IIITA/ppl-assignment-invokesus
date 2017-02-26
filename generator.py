import csv
from random import choice, randint
from string import ascii_lowercase

NO_OF_GIRLS = 10
NO_OF_BOYS = NO_OF_GIRLS * 5

Boyfriend_Types = ['Miser','Geek','Generous']
Girlfriend_Types = ['Choosy','Normal','Desperate']
Gift_Types = ['Essential','Luxury','Utility']

def create_csv (file, objects):
    write = csv.writer(open(file,"w"),delimiter = ',')

    for i in objects:
        write.writerow(i)

def create_name():
    return (''.join(choice(ascii_lowercase) for i in range(10)))

def generate():
    """

    Syntax of each row of boys.csv

    || Name || Attractiveness || Intelligence || Budget || Committed || Expenditure || Paired_To || Type_of_Boyfriend ||
        str      int <1,10>      int <1,10>  int <200,2000>  bool       int <0,2000>     str              str 

    """

    Boy = [(create_name(),randint(1,10),randint(1,10),randint(200,2000), False, 0, "", choice(Boyfriend_Types)) for i in range( NO_OF_BOYS )]

    """

    Syntax of each row of girls.csv

    || Name || Attractiveness || Intelligence || Maintenance || Committed || Paired_To || Type_of_Girlfriend ||
        str      int <1,10>      int <1,10>    int <200,2000>  bool         str              str

    """

    Girl = [(create_name(),randint(1,10),randint(1,10),randint(200,2000), False, "", choice(Girlfriend_Types))for i in range( NO_OF_GIRLS )]
    """

    Syntax of each row of gifts.csv

    || Name of Gift || Type_of_Gift || Price || Value || Luxury_Rating || Difficulty_to_Obtain || Utility_Class || Utility_Value ||
            str           str    int <50,2000> int <1,100> int <1, 10>      int <1, 10>               str              int<1,10>

    """

    Gift = [(create_name(), choice(Gift_Types), randint(50,2000), randint(1,100)) for i in range(1000)]

    create_csv('boys.csv',Boy)
    create_csv('girls.csv',Girl)
    create_csv('gifts.csv',Gift)

