import sys
import random
from models.Player import Player

def GAME_START():
    print("------------------LUCKY LAND GAME--------------------")


def choose_game_level():
    levels = {"SMALL": (1,2), "MEDIUM": (2,3), "LARGE": (3,4)}
    print("Chose your playground number:")
    for level in levels.items():
        print(f'{level[1][0]}.{level[0]}')
    input_number = 0
    try:
        input_number = int(input())
    except TypeError:
        print("Accept only number in range 1-3") 

    return [levels, input_number]


def next_move(all_cells_count):
    player_input = input('Press enter to continue the game or \'exit\' to stop:  ')
    possition = random.randint(1, all_cells_count-1)
    if player_input == "exit":
        sys.exit()
    return possition 


def check_health(player_one, player_two):
    if player_one.health <= 0:
        print(f'{player_two.name} is a Winner! {player_one.name} is dead!')
        return False
    elif player_two.health <= 0:
        print(f'{player_one.name} is a Winner! {player_two.name} is dead!')
        return False
    else:
        return True        


def END():
    print("-----------------GAME OVER-----------------")  