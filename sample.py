import keyboard
import time
from os import system


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])

def move(arr, curr_location, new_location): 
    arr[new_location[0]][new_location[1]] = arr[curr_location[0]][curr_location[1]]
    arr[curr_location[0]][curr_location[1]] = 0 

arr = [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ]

curr_location = [1,1]

print_arr(arr)

while (True):
    
    #print_arr(arr)
    if (keyboard.is_pressed("w") and curr_location[0] > 0):
        move(arr, curr_location, [ curr_location[0]-1, curr_location[1] ])
        curr_location = [ curr_location[0]-1, curr_location[1] ]
        system("clear")
        print_arr(arr)
        time.sleep(0.1)
    elif (keyboard.is_pressed("s")and curr_location[0] < 2):
        move(arr, curr_location, [ curr_location[0]+1, curr_location[1] ])
        curr_location = [ curr_location[0]+1, curr_location[1] ]
        system("clear")
        print_arr(arr)
        time.sleep(0.1)
    elif (keyboard.is_pressed("a") and curr_location[1] > 0):
        move(arr, curr_location, [ curr_location[0], curr_location[1]-1 ])
        curr_location = [ curr_location[0], curr_location[1]-1 ]
        system("clear")
        print_arr(arr)
        time.sleep(0.1)
    elif (keyboard.is_pressed("d") and curr_location[1] < 2):
        move(arr, curr_location, [ curr_location[0], curr_location[1]+1 ])
        curr_location = [ curr_location[0], curr_location[1]+1 ]
        system("clear")
        print_arr(arr)
        time.sleep(0.1)
    elif (keyboard.is_pressed("e")):
        break
    

'''             
while (True):

    #print_arr(arr)
    if (keyboard.is_pressed("w") and curr_location[0] > 0):
        move(arr, curr_location, [ curr_location[0]-1, curr_location[1] ])
        curr_location = [ curr_location[0]-1, curr_location[1] ]
        system("clear")
        print_arr(arr)
        time.sleep(0.1)
    elif (keyboard.is_pressed("s")and curr_location[0] < 2):
        move(arr, curr_location, [ curr_location[0]+1, curr_location[1] ])
        curr_location = [ curr_location[0]+1, curr_location[1] ]
        system("clear")
        print_arr(arr)
        time.sleep(0.1)
    elif (keyboard.is_pressed("a") and curr_location[1] > 0):
        move(arr, curr_location, [ curr_location[0], curr_location[1]-1 ])
        curr_location = [ curr_location[0], curr_location[1]-1 ]
        system("clear")
        print_arr(arr)
        time.sleep(0.1)
    elif (keyboard.is_pressed("d") and curr_location[1] < 2):
        move(arr, curr_location, [ curr_location[0], curr_location[1]+1 ])
        curr_location = [ curr_location[0], curr_location[1]+1 ]
        system("clear")
        print_arr(arr)
        time.sleep(0.1)
    elif (keyboard.is_pressed("e")):
        break


def move(arr, curr_location, new_location):
    arr[new_location[0]][new_location[1]] = arr[curr_location[0]][curr_location[1]]
    arr[curr_location[0]][curr_location[1]] = 0
'''
