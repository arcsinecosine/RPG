from player_classes import *
from enemy_classes import *
from util import *
from intro import *
from world_class import *
import pickle
import random
import csv
import os

global player
global world
global name_load

game_chooses = {
    1 : world.





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
                cls()
                name_load = intro()
                player = picke.load(open("%s.p" % (name_load) , "rb"))
                world = pickle.load(open("%s-world.p" %(name_load),"rb"))
                return (0)
            else:
                print ("That wasn't in range!")
                cls()
                continue





def game(player,world):
    while True:
        print_line()
        print ("MENU")
        print_line()
        print ("1. <<< EXPLORE <<< ")
        print_line()
        print ("2. <<< STATS <<< ")
        print_line()
        print ("3. <<< SAVE <<< ")
        print_line()
        print ("4. <<< QUIT <<< ")
        print_line()
        game_choice = int(input("Please enter a choice between 1-4"))
        if (0 < game_choice < 5):
            
    
    
        





if __name__ == "__main__":
    main()
