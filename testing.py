import pickle
import random
import csv
import os

cls = lambda: os.system("cls") #This function clears the screen
pause = lambda: os.system("pause") #This function paueses the screen

def read_script(x):  #This function prints out a text script line with pause
        with open('%s.txt' % (x) , newline='') as inputfile:
            for row in csv.reader(inputfile):
                print (row)
                pause()


def save(player): #This is the save function
    temp_username = str(player.name) #Assigns a new variable from instance variable of the players name
    if ((os.path.isfile("%s.p" % (temp_username)) == True )): #Checks for the existence of a previous safe file
        while True:
            temp_save_choice = input("This file exists already, would you like to overwrite? y/n") #Confirms overwriting
            temp_save_choice.lower()
            if (temp_save_choice == "y"): #Actually logs the save
                pickle.dump(player, open("%s.p" % (temp_username), "wb" )) #Pickle dump is written in bytes
                print ("Saved")
                return None
            elif (temp_save_choice == "n"): #Cancels save
                return ("Save wasn't made")
            else:
                return ("ERROR")
    else:
        pickle.dump(player, open("%s.p" % (temp_username) , "wb" )) #Logs the save
        return None


def load(): #load function in work
    temp_load_input = input("Please your characters name!")
    temple_load_input.lower()
    if ((os.path.isfile("%s.p" % (temp_load_input)) == True )):





def print_line(): #This function prints a line
    print ("----------")
    return None

class world:    #This class defines the world object
    def __init__(self):
        self.timedict = {1 : "9:00" , 2 : "3:00" , 3 : "7:00"} #dict value
        self.time = 0  # Sets the current time value at 0 before dungeon
        
class player: #Defines the superclass 
    def add_xp(self,bonus_xp): #This function adds the xp to the player
        self.xp = self.xp + bonus_xp
        while (self.xp >= 100):
            self.level_up()
            self.xp -= 100
        return None
    def level_up(self): #This function just increments the level by 1
        self.lvl += 1
    
class warrior(player): #Defines the warrior class
    def __init__(self,name): #takes in the name argument
        self.name = name #The following define the stats
        self.hp = 100
        self.mp = 50
        self.xp = 0
        self.dex = 3
        self.lvl = 1
        self.cls = "warrior"

class mage: #Defines the mage class
    def __init__(self,name): #takes in the name argument
        self.name = name #The following defines the stats 
        self.hp = 70
        self.mp = 100
        self.xp = 0
        self.dex = 3
        self.lvl = 1
        self.cls = "mage"

class rogue: #Defines the rogue class
    def __init__(self,name): #takes in the name argument
        self.name = name #The below defines the stats
        self.hp = 100
        self.mp = 50
        self.xp = 0
        self.dex = 3
        self.lvl = 1
        self.cls = "rogue"

class wchicken:
    def __init__(mob,mobname): #Chicken classes for Chicken Mobs ~Implemented by Jihad
        mob.mobname = "Warrior Chicken"
        mob.hp = 55
        mob.mp = 0
        mob.dex = random.randint(3,4)
        mob.lvl = random.randint(1,2)

class mchicken:
    def __init__(mob, mobname):
        mob.mobname = "Mage Chicken"
        mob.hp = 40
        mob.mp = 30
        mob.dex = 3
        mob.lvl = random.randint(1,2)
class rchicken:
    def __init__(mob,mobname):
        mob.mobname = "Rogue Chicken"
        mob.hp = 40
        mob.mp = 40
        mob.dex = random.randint(5,6)
        mob.lvl = random.randint(1,2)

def intro(): #This defines the intro of the game
    generic_warrior = warrior("generic")
    generic_mage = mage("generic")
    generic_rogue = rogue("generic")
    while True: #This is to make sure the username isn't blank
        temp_name = input("Please enter your name!")
        if (temp_name == ""):
            continue
        else:
            break
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
    while True:
        temp_choice = int(input("Please enter a number 1-3, depending on your class"))
        if ( 0 < temp_choice < 4 ):
            break
        else:
            continue

    if (temp_choice == 1):
        global player = warrior(temp_name)
    elif (temp_choice == 2):
        global player = mage(temp_name)
    else:
        global player = rogue(temp_name)
    temp_name_save = temp_name.lower()
    pickle.dump(player,open("%s.p" % (temp_name_save), "wb"))
    print ("Done!")
    
            



                          
def main():
    while True: #This prints out the menu
        print_line()
        print ("Welcome to our RPG")
        print_line()
        print ("1.Start a new game")
        print_line()
        print ("2.Load a game")
        print_line()
        print ("3.Quit Game")
        print_line()
        print ("Created by Benjamin Lodzhevsky,Jihad Beydoun, and Jonathan Ruvinov")
        print_line()
        while True:
            menu_choice = int(input("Please input a choice from a range of 1-3"))
            if ( menu_choice == 1 ):
                
            else:
                print ("That wasn't in range!")
                continue
        

def game_state(x):
        if (x == 1):
                intro()

    

