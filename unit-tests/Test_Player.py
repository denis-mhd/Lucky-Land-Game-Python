import unittest
import pytest
import sys
sys.path.append("..")
from models.Player import *

class Test_Player(unittest.TestCase):

    def setUp(self):
        self.obj_1 = Player("Ivan", 50, 2, 16) 
    
    def test_initial_values_Player(self):
        assert self.obj_1.name == "Ivan"
        assert self.obj_1.health == 50
        assert self.obj_1.current_cell == 2
        assert self.obj_1.all_cells_count == 16

    def test_initial_no_value(self):
        with pytest.raises(Exception) as e_info:
            obj = Player()      

    def test_add_health(self):
        self.obj_1.add_health(50)
        assert self.obj_1.health == 100

    def test_take_damage(self):
        self.obj_1.take_damage(20)
        assert self.obj_1.health == 30

    def test_move(self):
        self.obj_1.move()
        assert self.obj_1.current_cell > 0 
        assert self.obj_1.current_cell < 16

    #this test will requre user input (name) to create two players
    def test_create_players(self):
        players = Player.create_players(16)
        assert players[0].health == 100
        assert players[0].current_cell == 1
        assert players[0].all_cells_count == 16
        assert players[1].health == 100
        assert players[1].current_cell == 2
        assert players[1].all_cells_count == 16


if __name__ == '__main__':
    unittest.main()