from player_classes import *
from enemy_classes import *
from util import *
from intro import *
from world_class import *
import pickle
import random
import csv
import os
import pygame
from battle_func import *
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
a1 = pygame.mixer.Sound("a1.wav")
b1 = pygame.mixer.Sound("b1.wav")
c1 = pygame.mixer.Sound("c1.wav")

global player
global name_load
global game_loads





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
                player = pickle.load(open("%s.p" % (name_load) , "rb"))
                game(player)
            elif (menu_choice == 2):
                cls()
                while True:
                    game_loads = input("Please enter your name or type quit to quit!")
                    game_loads.lower()
                    if (game_loads == "quit"):
                        exit(420)
                    elif (game_loads == ""):
                        print ("No name typed please enter a valid name!")
                        pause()
                        cls()
                        continue
                    else:
                        if ((os.path.isfile("%s.p" % (game_loads)) == True)):
                            player = load(game_loads)
                            game(player)
                        else:
                            continue
            elif (menu_choice == 3):
                print ("quitting!")
                pause()
                exit(11)
            else:
                print ("That wasn't in range!")
                cls()
                continue





def game(player):
    while True:
        print_line()
        print ("MENU")
        print_line()
        print ("1. <<< EXPLORE <<< ")
        print_line()
        print ("2. <<< PUZZLE <<< ")
        print_line()
        print ("3. <<< SAVE <<< ")
        print_line()
        print ("4. <<< QUIT <<< ")
        print_line()
        try:
            game_choice = int(input("Please enter a choice between 1-4"))
        except:
            print ("Not in range!!!!!!!")
            continue
        if (0 < game_choice < 5):
            if (game_choice == 1):
                if (player.story1 == False):
                    story_event1(player)
                    cls()
                    continue
                elif (player.story2 == False):
                    story_event2(player)
                    cls()
                    continue
                elif (player.story3 == False):
                    story_event3(player)
                    cls()
                    continue
                else:
                    print ("ALL STORIES EVENT DONE! THANK YOU FOR PLAYING")
            elif (game_choice == 2):
                if (player.puzzle1 == False):
                    puzzle_event1(player)
                    cls()
                    continue
                elif (player.puzzle2 == False):
                    puzzle_event2(player)
                    cls()
                    continue
                elif (player.puzzle3 == False):
                    puzzle_event3(player)
                    cls()
                    continue
                else:
                    print ("ALL PUZZLES ARE DONE")
                    cls()
                    continue
            elif (game_choice == 3):
                print ("Saving......")
                save(player)
                pause()
                cls()
                continue
            elif (game_choice == 4):
                print ("quitting....")
                quit(455)
        else:
            print ("Not in range!!!!!!!!")

            
    
    
        



def story_event1(player):
    read_file(2)
    battle(player,)


def story_event2(player):
    read_file(3)
    pass

def story_event3(player):
    read_file(4)
    pass



def puzzle_event1(player):
    print ("You are now stopped by a huge chicken and he tells you that he will give you mercy only if you answer his riddle correctly!")
    while True:
        print ("Solve for x:  2(x+6)=36")
        answer = int(input(""))
        if (answer == 12):
            print ("The chicken says, 'Congrats on solving my puzzle traveler!'")
            print ("In return I will increase your strength by 1")
            player.str += 1
            player.puzzle1 = True
            return None
        else:
            print ("That is wrong! I will give you 1 more chance!")
            continue

def puzzle_event2(player):
    print ("You are now stopped by a huge chicken and he tells you that he will give you mercy only if you answer his riddle correctly!")
    while True:
        print ("Solve for x:  -3+5x=12")
        answer = int(input(""))
        if (answer == 3):
            print ("The chicken says, 'Congrats on solving my puzzle traveler!'")
            print ("In return I will increase your magic strength by 1")
            player.ms += 1
            player.puzzle2 = True
            return None
        else:
            print ("That is wrong! I will give you 1 more chance!")
            continue


def puzzle_event3(player):
    print ("You are now stopped by a huge chicken and he tells you that he will give you mercy only if you answer his riddle correctly!")
    while True:
        print ("Solve for b:  3b+6=-18")
        answer = float(input(""))
        if (answer  == -3):
            print ("The chicken says, 'Congrats on solving my puzzle traveler!'")
            print ("In return I will increase your dexterity by 1")
            player.dex += 1
            player.puzzle3 = True
            return None
        else:
            print ("That is wrong! I will give you 1 more chance!")
            continue



















if __name__ == "__main__":
    main()
    # 8=============D ~~~~~