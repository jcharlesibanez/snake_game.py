import random
import os

def askForSize():
    side_length = int(input("How big should the playing-zone be? (>=10): "))
    while type(side_length) != int:
        side_length = int(input("Please enter a number greater than or equal to 10: "))
    while side_length < 10:
        side_length = int(input("The playing-zone square must have side lengths at least 10 chars long: "))
    return side_length

def buildPlayingZone(arr):
    for i in range(len(arr[0])):
        print(arr[i])

def move(arr, dir, pos):
    snake_head_row = pos//len(arr[0])
    snake_head_column = arr[snake_head_row].index("X")
    if dir == "up":
        arr[snake_head_row-1][snake_head_column] = "X"
        arr[snake_head_row][snake_head_column] = "O"
    elif dir == "down":
        arr[snake_head_row+1][snake_head_column] = "X"
        arr[snake_head_row][snake_head_column] = "O"
    elif dir == "right":
        arr[snake_head_row][snake_head_column+1] = "X"
        arr[snake_head_row][snake_head_column] = "O"
    elif dir == "left":
        arr[snake_head_row][snake_head_column-1] = "X"
        arr[snake_head_row][snake_head_column] = "O"
    buildPlayingZone(arr)

def progress(arr, iter):
    valid_responses = ['up', 'down', 'left', 'right']
    while iter >= 0:
        dir = input("say 'up', 'down', 'left', or 'right': ")
        while dir not in valid_responses:
            dir = input("say 'up', 'down', 'left', or 'right': ")
        os.system('cls')
        for row in arr:
            for item in row:
                if item == "X":
                    pos = arr.index(row) * len(arr[0]) + arr[arr.index(row)].index(item)
        move(arr, dir, pos)
        iter -= 1

def play(s):
    starting_position = random.randint(0, s**2 - 1)
    apple_position = random.randint(0, s**2 - 1)
    while apple_position == starting_position:
        apple_position = random.randint(0, s**2 - 1)
    playing_zone_array = [["O" for row in range(s)] for column in range(s)]
    playing_zone_array[starting_position//s-1][starting_position%s] = "X"
    playing_zone_array[apple_position//s-1][apple_position%s] = "!"
    buildPlayingZone(playing_zone_array)
    progress(playing_zone_array, 10)

def main():
    play(askForSize())

main()