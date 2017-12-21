from enemy_classes import *
from random import *
from util import *


def battle(player,enemy):
    if (enemy == 1):
        battle_enemy = wchicken()
    elif (enemy == 2):
        battle_enemy = mchicken()
    elif (enemy == 3):
        battle_enemy = rchicken()
    else:
        print ("ERROR NO ENEMY")
        exit(420)

    while (battle_enemy.hp > 0):
        print ("1. <<< ATTACK <<< ")
        print ("2. <<< ITEM <<< ")
        print ("3.. <<< CURRENT HEALTH: %d <<< " % (int(player.hp)))
        try:
            battle_choice = int(input("Please enter 1 or 2"))
        except:
            print ("NOT IN RANGE FAM")
            continue
        if (battle_choice == 1):
            player.print_attacks()
            print ("Please enter 1 or 2")
            try:
                attacks_choice = int(input(""))
            except:
                print ("Not in range!")
                continue
            if ( 0 < attacks_choice < 3):
                print ("ATTACKING!!!")
                print ("You did:" + str(player.attacks[attacks_choice]) + " amount of damage")
                user_attack = player.attacks[attacks_choice]
                battle_enemy.hp = battle_enemy.hp - user_attack
                enemy_attack = battle_enemy.rand_attack()
                print (enemy_attack)
                true_enemy_attack = battle_enemy.attacks[enemy_attack]
                print ("The enemy is going to do this amount of damage!" + str(true_enemy_attack))
                player.hp = player.hp - true_enemy_attack
                print ("HP: " + str(player.hp))

                if (player.hp <= 0):
                    print ("Game over!")
                    pause()
                    exit(455)
                else:
                    cls()
                    continue
        elif (battle_choice == 2):
            if (player.pot > 0):
                while True:
                    print ("You currently have %d pots" % int(player.pot))
                    print ("Would you like to use a pot?")
                    try:
                        pot_choice = int(input("Please enter 1(y) or 2(n)"))
                    except:
                        print("Not in range!")
                        cls()
                        continue
                    if (pot_choice == 1):
                        print ("Health added!")
                        player.hp += 20
                        player.pot -= 1
                        break

                    elif (pot_choice == 2):
                        print ("Cancelling!")
                        break
            else:
                print ("No pots!")
                continue

            continue




        
