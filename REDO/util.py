import csv

def print_line(): #This function prints a line
    print ("----------")
    return None

def save(player,world): #This is the save function
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
    with open("%s.txt" , "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            temp_string = row
            print (temp_string)



