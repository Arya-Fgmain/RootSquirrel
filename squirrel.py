# Arya Faghihy
# Mar 4, 2023

import keyboard
import time
import random
from os import system

''' Functions '''

def print_map(map):
    for i in range(len(map)):
        print(map[i])

# moveRight and moveLeft move the character sprite 
# one character to the right/;eft

def moveRight(map, currPos):
    map[3] = "|" + " " * (currPos) + character1 + " " * (14-currPos) + "|"
    map[4] = "|" + " " * (currPos) + character2 + " " * (14-currPos) + "|"
    map[5] = "|" + " " * (currPos) + character3 + " " * (14-currPos) + "|"


def moveLeft(map, currPos):
    map[3] = "|" + " " * (currPos-1) + character1 + " " * (15-currPos) + "|"
    map[4] = "|" + " " * (currPos-1) + character2 + " " * (15-currPos) + "|"
    map[5] = "|" + " " * (currPos-1) + character3 + " " * (15-currPos) + "|"        

# updates the map by randomly spawning a nut in the top row
# and replacing the 2nd and 3rd rows with each other

def map_update(map):
    nut_pos = random.randint(1,23)
    map[2] = map[1]
    map[1] = map[0]
    map[0] = "|" + " " * (nut_pos) + "n" + " " * (22-nut_pos) + "|"
    return nut_pos

# strings to represent the map and character
base = "|" + " " * 23 + "|";
character1 = "[-------]"
character2 = "[  (00) ]"
character3 = "[   --  ]"
char1 = "|       " + character1 + "       |"
char2 = "|       " + character2 + "       |"
char3 = "|       " + character3 + "       |"

# string array to represent the whole map
map = [ base, base, base, char1, char2, char3 ]

# horizontal position of the character (top-left corner) in the map
curr_pos = 8

# nut position given default value (updated once a nut is spawned)
nut_position = -1

# nut's distance from the character, used to check
# for collision
distance_from_nut = 3

score = 0


print_map(map)

''' Main Game Loop '''

while (True and score <= 20): 
    # after moving the character, clear the terminal
    # and print the score each time
    # time.sleep() is used to delay input, otherwise
    # the same keyboard press might be taken as input
    # multiple times

    if (keyboard.is_pressed("d") and curr_pos < 15):
        moveRight(map, curr_pos)
        curr_pos += 1
        system("clear")
        print("SCORE: " + str(score))
        # nut's distance from the character, used to check
        # # for collisionr(score))
        if distance_from_nut == 0 and (nut_position >= curr_pos
                               or nut_position <= curr_pos+8):
            score += 1
        else:
            # nut's distance from the character, used to check
            # for collision
            distance_from_nut -= 1
        print_map(map)
        time.sleep(0.1)
    elif (keyboard.is_pressed("a") and curr_pos > 0):
        moveLeft(map, curr_pos)
        curr_pos -= 1
        system("clear")
        print("SCORE: " + str(score))
        # nut's distance from the character, used to check
        # # for collisionr(score))
        if distance_from_nut == 0 and (nut_position >= curr_pos
                               or nut_position <= curr_pos+8):
            score += 1
        else:
            # nut's distance from the character, used to check
            # for collision
            distance_from_nut -= 1
        print_map(map)
        time.sleep(0.1)
    elif (keyboard.is_pressed("e")):
        break
    # update the map after every iteration
    nut_position = map_update(map)

system("clear") # clears any input left
print("Congradulations! You win!")
                

            
