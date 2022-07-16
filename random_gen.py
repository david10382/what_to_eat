import random
from data import menu

def menu_random():
    # convert dict to array
    #print(list(menu.keys()))
    print("Be adventrous and find or make:", random.choice(list(menu.keys())))