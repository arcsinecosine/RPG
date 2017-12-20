from enemy_classes import *


def battle(player,enemy):
    user_attack = None
    enemy_attack = None
    true_enemy_attack = None
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
                print ("You did:" + player.attacks[attacks_choice] + "amount of damage")
                user_attack = player.attacks[attacks_choice]
                battle_enemy.hp = battle_enemy.hp - user_attack
                enemy_attack = battle_enemy.rand_attack
                true_enemy_attack = battle_enemy.attacks[enemy_attack]
                print ("The enemy is going to do this amount of damage!" + true_enemy_attack)
                player.hp = player.hp - true_enemy_attack
                print ("HP: " + player.hp)
                if (player.hp <= 0):
                    print ("Game over!")
                    pause()
                    exit(455)
                else:
                    pass
            else:
                print ("Not in range!")
                pause()
                cls()
                continue







        
