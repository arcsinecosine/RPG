class world:    #This class defines the world object
    def __init__(self):
        self.timedict = {1 : "9:00" , 2 : "3:00" , 3 : "7:00"} #dict value
        self.time = 0  # Sets the current time value at 0 before dungeon
        
class warrior: #Defines the warrior class
    def __init__(self,name): #takes in the name argument
        self.name = name #The following define the stats
        self.hp = 100
        self.mp = 50
        self.exp = 0
        self.dex = 3
        self.lvl = 1
        self.cls = "warrior"

class mage: #Defines the mage class
    def __init__(self,name): #takes in the name argument
        self.name = name #The following defines the stats 
        self.hp = 70
        self.mp = 100
        self.exp = 0
        self.dex = 3
        self.lvl = 1
        self.cls = "mage"

class rogue: #Defines the rogue class
    def __init__(self,name): #takes in the name argument
        self.name = name #The below defines the stats
        self.hp = 100
        self.mp = 50
        self.exp = 0
        self.dex = 3
        self.lvl = 1
        self.cls = "rogue"
                



