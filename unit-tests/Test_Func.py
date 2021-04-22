import unittest
import pytest
import sys
sys.path.append("..")
from Func import *
from models.Cell import *
from unittest import mock
from InputOutput import *
from models.Player import *
from models.CardFactory import *

class Test_Func(unittest.TestCase):
    
    def setUp(self):
        self.player_one = Player("Gosho", 50, 2, 16)
        self.player_two = Player("Misho", 50, 2, 16)
        self.player_three = Player("Misho", 20, 2, 16)
        self.player_four = Player("Misho", 0, 2, 16)
        self.cards = [GoodCard(), BadCard(), TripCard()]
        self.field =[[{1:Cell(0,0,self.cards)}, {2:Cell(0,1,self.cards)}]]
        self.levels = {"SMALL": (1,2), "MEDIUM": (2,3), "LARGE": (3,4)}

    def test_get_cells_count_on_row_selected_SMALL(self):
        assert get_cells_count_on_row(self.levels, 3) == 4
        
    def test_get_cells_count_on_row_selected_MEDIUM(self):
        assert get_cells_count_on_row(self.levels, 2) == 3

    @mock.patch("Func.random.randint", return_value = 2)
    def test_get_card(self, mock_randint):
        assert type(get_card(self.field, 2)) == type(TripCard())


    def test_war_with_equal_players_health(self):
        war(self.player_one, self.player_two)
        assert self.player_one.health == 25
        assert self.player_two.health == 25

    def test_war_with_different_players_health(self):
        war(self.player_one, self.player_three)
        assert self.player_one.health == 49
        assert self.player_three.health == 5 

      

if __name__ == '__main__':
    unittest.main()