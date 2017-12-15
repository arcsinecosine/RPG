from enemy_classes import *


def battle(player,enemy):
    if (enemy == 1):
        battle_enemy = wchicken()
    elif (enemy == 2):
        battle_enemy = mchicken()
    elif (enemy == 3):
        battle_enemy == rchicken()
    else:
        print ("ERROR NO ENEMY")
        exit(420)
    while (battle_enemy.hp > 0):
        print ("1. <<< ATTACK <<< ")
        print ("2. <<< ITEM <<< ")
        battle_choice = int(input("Please enter 1 or 2"))
        if 
        
