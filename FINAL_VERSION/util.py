import csv
import os
import pickle

cls = lambda: os.system("cls") #This function clears the screen
pause = lambda: os.system("pause") #This function paueses the screen

def print_line(): #This function prints a line
    print ("----------")
    return None

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

def read_file(x):
    x = str(x)
    with open("%s.txt" % (x), "r") as f:
        reader = csv.reader(f)
        for row in reader:
            temp_string = row
            print (temp_string)


def load(x):
    temp_str = str(x)
    temp_str.lower()
    fp = open("%s.p" % (temp_str) , "rb")
    loaded_player = pickle.load(fp)
    return loaded_player

def load_world(x):
    temp_str = str(x)
    temp_str.lower()
    fp = open("%s-world.p" % (temp_str), "rb")
    return fp



