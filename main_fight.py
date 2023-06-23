import random
import enemies
from player import player
from enum import Enum

# ---------------------------Seperation for visual flow------------------------------------ #

# This code is used for better visibility throughout the code.
line = '-----------------\n'


# This code chooses a random enemy from the enemies.py file and saves it to the enemy variable. 
# The following print statements state which enemy we are fighting and their hitpoints
enemy = random.choice(enemies.enemies)

print(f"\n{player.name} vs. {enemy['name']}\n")
print(f"{player.name} - {player.hit_points} hitpoints")
print(f"{enemy['name']} - {enemy['hit_points']} hitpoints")
print("\nLet the battle commence..")


# -- Fight --

class PlayerMove(Enum):
    HEAL = 'h'
    ATTACK = 'a'

# The entire fight happens within this while loop. (While both the player and enemy are alive/ have above 0 hp)
while (player.hit_points > 0) and (enemy['hit_points'] > 0):
    
    # PLAYER TURN - This allows you to press the h or a key to heal or attack respectively 
    # if you attack it rolls a hit chance based on your accuracy and if you successfully hit then it rolls the damage based on your strength
    player_move = input(line + '(Your Turn. h: Heal, a: Attack)')
    print('')
    
    while player_move not in [move.value for move in PlayerMove]:
        player_move = input('(Invalid input, try again. h: Heal, a: Attack)\n')

    if player_move == PlayerMove.HEAL.value:
        if 'potion' in player.inventory:
            player.hit_points += 10
            print(f'You drink a potion\nYou have {player.hit_points} hit points remaining.\n')
            player.inventory.remove('potion')
        else:
            print('You have no available potions')
            continue
    elif player_move == PlayerMove.ATTACK.value:
        player_hit_chance = random.choice(range(0, player.accuracy))
        hit = player_hit_chance >= (player.accuracy / 2)

        if hit:
            hit = random.choice(range(1, player.strength))
            print(f'You hit a {hit}')
            enemy['hit_points'] -= hit

            if enemy['hit_points'] <= 0:
                print(f"{enemy['name']} has died.\n")
                continue
        else:
            print("You missed!")
        
        print(f"({enemy['name']} - {enemy['hit_points']} hit points remaining.)\n")


    # ENEMY TURN - This rolls the enemy hit chance based on their accuracy,
    # and if they hit it rolls how much they hit based on their strength.
    enemies.enemy_turn(enemy, player)


# You died.
if player.hit_points < 1:
    print("The battle concludes..")

# Assuming player defeats the enemy. This code rolls the drops for the defeated monster.
if enemy['hit_points'] < 1:
    enemies.looting(enemy, player)

