from player_classes import *
from enemy_classes import *
from util import *
from intro import *
from world_class import *
import pickle
import random
import csv
import os

cls = lambda: os.system("cls") #This function clears the screen
pause = lambda: os.system("pause") #This function paueses the screen

global player
global world

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
                player = intro()
                world = world()

            else:
                print ("That wasn't in range!")
                continue
        cls()
        




if __name__ == "__main__":
    main()
