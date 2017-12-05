class world:    #This class defines the world object
    def __init__(self):
        self.timedict = {1 : "9:00" , 2 : "3:00" , 3 : "7:00"} #dict value
        self.time = 0  # Sets the current time value at 0 before dungeon
        
class player:
    def add_xp(self,bonus_xp):
        self.xp = self.xp + bonus_xp
        while (self.xp >= 100):
            self.level_up()
            self.xp -= 100
        return None

        
    def level_up(self):
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

x = warrior("ben")

print (x.lvl)
x.level_up()
print (x.lvl)
x.add_xp(200)
print (x.lvl)

    


