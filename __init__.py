import random
from .Datas import *

import os
print("Current Working Directory:", os.getcwd())


# prastha_pirulu
def prastha_pirulu():
    return random.choice(Prastha_Pirulu_List)

# prastha_pirulu
def pp():
    return random.choice(Prastha_Pirulu_List)


# theravili
def theravili():
    return random.choice(theravili_List)

# thun_theravili
def thun_theravili():
    return random.choice(thun_theravili_List)


# thun_theravili shorts
def thun():
    return random.choice(thun_theravili_List)

def name_array(file):
    with open(file) as fp:
        new_list = []
        for line in fp:
            new_list.append(line.strip())
    return new_list


file = "male_first_names.txt"
male_names = name_array(file)

file = "female_first_names.txt"
female_names = name_array(file)

file = "last_names.txt"
last_names = name_array(file)

file = "home_address.txt"
home_address = name_array(file)

file = "city.txt"
city_name = name_array(file)


def quin():
    result = f"['Avihinsaka uwathy','Nihada Mawatha ','Palu Niwahana']"
    return result



def femalename():
    result = f"[{random.choice(female_names)} {random.choice(last_names)}]"
    return result



def femaleaddress():
    result = f"[{random.choice(female_names)} {random.choice(last_names)},{random.choice(home_address)},{random.choice(city_name)}]"
    return result



def maleaddress():
    result = f"['{random.choice(male_names)} {random.choice(last_names)}','{random.choice(home_address)}','{random.choice(city_name)}']"
    return result



