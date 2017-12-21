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
        self.str = 5
        self.ms = 2
        self.dex = 3
        self.lvl = 1
        self.cls = "warrior"
        self.pot = 3
        self.story1 = False
        self.story2 = False
        self.story3 = False
        self.puzzle1 = False
        self.puzzle2 = False
        self.puzzle3 = False
        self.attacks = {1 : self.str + self.dex , 2 : self.str + 1}

    def print_attacks(self):
        print ("1.SLASH")
        print ("2.STAB")

class mage: #Defines the mage class

    def __init__(self,name): #takes in the name argument
        self.name = name #The following defines the stats 
        self.hp = 70
        self.mp = 100
        self.xp = 0
        self.str = 2
        self.ms = 5
        self.dex = 3
        self.lvl = 1
        self.cls = "mage"
        self.pot = 3
        self.story1 = False
        self.story2 = False
        self.story3 = False
        self.puzzle1 = False
        self.puzzle2 = False
        self.puzzle3 = False
        self.attacks = {1: self.str , 2: self.ms + 4}

    def print_attacks(self):
        print ("1.SWING")
        print ("2.FIREBALL")


class rogue: #Defines the rogue class

    def __init__(self,name): #takes in the name argument
        self.name = name #The below defines the stats
        self.hp = 100
        self.mp = 50
        self.xp = 0
        self.str = 3
        self.ms = 3
        self.dex = 5
        self.lvl = 1
        self.cls = "rogue"
        self.pot = 3
        self.story1 = False
        self.story2 = False
        self.story3 = False
        self.puzzle1 = False
        self.puzzle2 = False
        self.puzzle3 = False
        self.attacks = {1: self.str + self.dex, 2: self.dex + 3}

    def print_attacks(self):
        print ("1.SLASH")
        print ("2.ASSASINATE")

