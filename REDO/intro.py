from player_classes import *
from util import *
import pickle
from lamb_func import *

def print_classes():
    generic_warrior = warrior("generic")
    generic_mage = mage("generic")
    generic_rogue = rogue("generic")
    print ("These are the classes") #The lines below are just defined the stats 
    print_line()                    # of each class
    print ("CLASSES")
    print_line()
    print ("1.Warrior Stats")
    print_line()
    print ("Health Points:" + str(generic_warrior.hp))
    print ("Magic Points:" + str(generic_warrior.mp))
    print ("Dexterity Points" + str(generic_warrior.dex))
    print_line()
    print ("2.Mage Stats")
    print_line()
    print ("Health Points:" + str(generic_mage.hp))
    print ("Magic Points:" + str(generic_mage.mp))
    print ("Dexterity Points" + str(generic_mage.dex))
    print_line()
    print ("3.Rogue Stats")
    print_line()
    print ("Health Points:" + str(generic_warrior.hp))
    print ("Magic Points:" + str(generic_warrior.mp))
    print ("Dexterity Points" + str(generic_warrior.dex))
    print_line()

def intro(): #This defines the intro of the game
    while True: #This is to make sure the username isn't blank
        temp_name = input("Please enter your name!")
        if (temp_name == ""):
            continue
        else:
            break
    read_file(1)
    print_classes()
    
    while True:
        temp_choice = int(input("Please enter a number 1-3, depending on your class"))
        if ( 0 < temp_choice < 4 ):
            break
        else:
            continue

    if (temp_choice == 1):
        player = warrior(temp_name)
    elif (temp_choice == 2):
        player = mage(temp_name)
    else:
        player = rogue(temp_name)
    temp_name_save = temp_name.lower()
    pickle.dump(player,open("%s.p" % (temp_name_save), "wb"))
    world = world()
    pickle.dump(world,open("%s-world.p" % (temp_name_save), "wb"))
    print ("Done!")
    return (temp_name_save)
