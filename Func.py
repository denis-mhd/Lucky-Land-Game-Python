import random
from models.Playground import Playground    

def get_cells_count_on_row(levels, input_number):
    selected_size = [val[1] for val in levels.values() if val[0] == input_number]
    cells_count_on_row = selected_size[0]
    return cells_count_on_row


def get_card(plain_field, possition):
    for row in range(0, len(plain_field)):
        for col in range(0, len(plain_field[row])):
            dic = plain_field[row][col]
            key = list(dic)[0]
            if possition == key:
                c = dic.get(key)
                cards_count = len(c.cards)
                i = random.randint(0, cards_count-1)
                card = c.cards[i]
    return card            


def war(player1, player2):
    print("----------------WAR!!!----------------")
    if (player1.health > player2.health):
        strong_player = player1
        weak_player = player2
    elif player1.health == player2.health:
        damage = int(0.5*player1.health)
        player1.take_damage(damage)
        player2.take_damage(damage)
        return
    else:
        strong_player = player2
        weak_player = player1  

    weak_player_damage = int(0.5*(player1.health - player2.health)) 
    weak_player.take_damage(weak_player_damage)
    strong_player_damage = int(0.25*player2.health)
    strong_player.take_damage(strong_player_damage)            

