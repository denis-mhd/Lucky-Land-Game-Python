import random

class Player:

    def __init__(self, name, health, current_cell, all_cells_count):
        self.name = name
        self.health = health
        self.current_cell = current_cell
        self.all_cells_count = all_cells_count

    def add_health(self, health_points):
        self.health += health_points
        print(f'{self.name} take extra health {health_points}. Current health {self.health} points')    

    def take_damage(self, damage):
        self.health -= damage
        print(f'{self.name} take damage {abs(damage)} points. {self.health} points left')    

    def move(self):
        given_cell = random.randint(1, self.all_cells_count - 1)
        self.current_cell = given_cell
        print(f'{self.name} move on cell number {given_cell}')

    @staticmethod
    def create_players(all_cells_count):
        player_one_name = input('Enter first player\'s name: ')
        player_one = Player(player_one_name, 100, 1, all_cells_count)
        player_two_name = input('Enter second player\' name: ')
        player_two = Player(player_two_name, 100, 2, all_cells_count)
        return [player_one, player_two]