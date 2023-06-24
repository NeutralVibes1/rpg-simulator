import random

# This file contains a dictionary of all of the current enemy options. Each enemy dictionary contains a name, hitpoints, loot (dictionary), strength, and accuracy

enemies = {0: {'name': 'Goblin', 'hit_points': 50, 'loot': {100: 'bones', 50: 'shield', 25: 'helmet'}, 'strength': 5, 'accuracy': 20},
           1: {'name': 'Ogre', 'hit_points': 100, 'loot': {100: 'bones', 50: 'club', 25: 'ogre headpiece', 5: 'ogre kilt'}, 'strength': 12, 'accuracy': 7},
           2: {'name': 'Dark Wizard', 'hit_points': 75, 'loot': {100: 'bones', 50: 'robe', 25: 'talisman'}, 'strength': 7, 'accuracy': 12},
           3: {'name': 'Malwok, The Chained', 'hit_points': 750, 'loot': {100: 'huge bones', 75: "Malwok's Robe"}, 'strength': 30, 'accuracy': 5}}


def add_enemy(id, name, hit_points, loot, strength, accuracy):
    enemies[id] = {'name':name, 'hit_points': hit_points, 'loot': loot, 'strength': strength, 'accuracy': accuracy}


# Fight-related functions:
def enemy_turn(enemy, player, defend):
    enemy_hit_chance = (random.choice(range(0, enemy['accuracy'])))
    if defend == 'defend':
        enemy_hit_chance -= (enemy['accuracy'] / 4)
    enemy_hit = enemy_hit_chance >= (enemy['accuracy'] / 2)
    enemy_hit_pwr = random.choice(range(1, enemy['strength']))
       
    if enemy_hit:
        print(f"{enemy['name']} hit a {enemy_hit_pwr}")
        player.hit_points = player.hit_points - enemy_hit_pwr

        if player.hit_points <= 0:
            print("You have died.\n")
    else:
        print(f"{enemy['name']} Missed!")
        
    print(f"({player.name} - {player.hit_points} hit points remaining.)\n")


def looting(enemy, player):
    loot = enemy['loot']
    roll = random.choice(range(1, 100))

    for item in loot.items():
        chance = item[0]
        item = item[1]
        if roll <= chance:
            print(f'You found {item}')
            player.inventory.append(item)

    print(player.inventory)
