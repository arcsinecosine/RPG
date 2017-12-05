import pickle

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

def intro():
    temp_name = input("Please enter your name!")
    generic_warrior = warrior("sample")
    generic_mage = mage("sample")
    generic_rogue = rogue("sample")
    print_line()
    print ("CLASSES")
    print_line()
    print ("Warrior")
    print_line()
    print ("Health Points:" + str(generic_warrior.hp))
    print ("Magic Points:" + str(generic_warrior.mp))
    print ("Dexterity Points: " + str(generic_warrior.dex))
    print_line()
    print ("Mage")
    print_line()
    print ("Health Points:" + str(generic_mage.hp))
    print ("Magic Points" + str(generic_mage.mp))
    print ("Dexterity Points" + str(generic_mage.dex))
    print_line()


intro()


    

