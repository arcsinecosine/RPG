from random import *

class super_chicken:

    def rand_attack(self):
        temp_intger = randint(1,2)
        return temp_intger


class wchicken(super_chicken):

    def __init__(self): #Chicken classes for Chicken Mobs ~Implemented by Jihad
        self.mobname = "Warrior Chicken"
        self.hp = 55
        self.mp = 0
        self.dex = randint(3,4)
        self.attacks = {1 : 4 , 2 : 2}    #This attack is peck






class mchicken:
    def __init__(self):
        self.mobname = "Mage Chicken"
        self.hp = 40
        self.mp = 30
        self.dex = 3
        self.attacks = {1 : 4 , 2 : 2}   #This attack is fireball




class rchicken:
    def __init__(self):
        self.mobname = "Rogue Chicken"
        self.hp = 40
        self.mp = 40
        self.dex = randint(5,6)
        self.attacks = {1 : 4 , 2 : 2}  #This attack is rogue peck idk



