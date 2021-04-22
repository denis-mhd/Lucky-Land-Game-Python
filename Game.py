import sys
from Func import *
from InputOutput import *
from models.CardFactory import *

GAME_START()

levels_result = choose_game_level()
levels = levels_result[0]
input_number = levels_result[1]

cells_count_on_row = get_cells_count_on_row(levels, input_number)
total_matrix_cells_count = cells_count_on_row*cells_count_on_row
playground = Playground(cells_count_on_row)
field = playground.build_playground()

players = Player.create_players(total_matrix_cells_count)
player_one = players[0]
player_two = players[1]

is_alive = True
while is_alive:
    
    if player_one.current_cell == player_two.current_cell:
        war(player_one, player_two)
        is_alive = check_health(player_one, player_two)
        if not is_alive:
            break
            
    for player in players:
        possition = next_move(total_matrix_cells_count)
        lucky_card = get_card(field, possition)
        lucky_card.action(player)
        
    is_alive = check_health(player_one, player_two)    

END()        
  




        






    

    


