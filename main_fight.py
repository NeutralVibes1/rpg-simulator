import random
import enemies
import player

# ---------------------------Seperation for visual flow------------------------------------ #

# This code is used for better visibility throughout the code.
line = '-----------------\n'


# This code chooses a random enemy from the enemies.py file and saves it to the enemy variable. The following print statements state which enemy we are fighting and their hitpoints
enemy = random.choice(enemies.enemies)

print("\n" + player.name + " vs. " + enemy['name'] + "\n")
print('{0} - {1} hitpoints'.format(player.name, player.hit_points))
print('{0} - {1} hitpoints'.format(enemy['name'], enemy['hit_points']))
print('\nLet the battle commence..')


# Player turns - This allows you to press the h or a key to heal or attach respectively, if you heal your hit points raise by 10, if you attack it rolls a hit chance
# Based on your accuracy and if you successfully hit then it rolls the damage based on your strength
while (player.hit_points > 0) and (enemy['hit_points'] > 0):
    player_move = input(line + '(Your Turn. h: Heal, a: Attack)')
    print('')
    
    if player_move != 'h' and player_move != 'a':
        player_move = input('(Invalid input, try again. h: Heal, a: Attack)')
        print('')

    if player_move == 'h':
        player.hit_points += 10
        print('You drink a potion\n' + 'You have ' + str(player.hit_points) + ' hitpoints remaining.\n')

    elif player_move == 'a':
        player_hit_chance = (random.choice(range(0, player.accuracy)))
        hit = None
    
        if player_hit_chance >= (player.accuracy / 2):
            hit = True
        elif (player_hit_chance < (player.accuracy / 2)) or (player.hit_points < 0):
            hit = False

        if hit:
            hit = random.choice(range(1, 15))
            print("You hit a {hit}".format(hit=hit))
            enemy['hit_points'] = enemy['hit_points'] - hit

            if enemy['hit_points'] <= 0:
                print(enemy['name'] + " has died.\n")
                continue
            print('(' + enemy['name'], "-", str(enemy['hit_points']) + " hit points remaining.)\n")
        elif hit is False:
            print("You missed!")
            print('(' + enemy['name'], "-", str(enemy['hit_points']) + " hit points remaining.)\n")


    # Enemy turns - This rolls the enemy hit chance based on their accuracy and if they hit it rolls how much they hit based on their strength
    enemy_hit_chance = (random.choice(range(0, enemy['accuracy'])))
    enemy_hit = None

    if enemy_hit_chance >= (enemy['accuracy'] / 2):
        enemy_hit = True
    elif (enemy_hit_chance < (enemy['accuracy'] / 2)) or (enemy['hit_points'] <= 0):
        enemy_hit = False

    if enemy_hit:
        enemy_hit = random.choice(range(1, enemy['strength']))
        print(enemy['name'], "hit a " + str(enemy_hit))
        player.hit_points = player.hit_points - enemy_hit

        if player.hit_points <= 0:
            print("You have died.\n")
            continue
        print('(' + player.name, "-", str(player.hit_points) + " hit points remaining.)\n")

    elif enemy_hit is False:
        print(enemy['name'], "Missed!")
        print('(' + player.name, "-", str(player.hit_points) + " hit points remaining.)\n")


# You died.
if player.hit_points < 1:
    print("The battle concludes..")

# Assuming player defeats the enemy. This code rolls the drops for the defeated monster
if enemy['hit_points'] < 1:
    loot = enemy['loot']
    roll = random.choice(range(1, 100))

    for item in loot.items():
        chance = item[0]
        item = item[1]
        if roll <= chance:
            print('You found ' + item)
            player.inventory.append(item)

    print(player.inventory)

