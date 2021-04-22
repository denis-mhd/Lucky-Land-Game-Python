import unittest
from unittest import mock
import pytest
import sys
sys.path.append("..")
from models.Player import *
from InputOutput import *

class Test_InputOutput(unittest.TestCase):
    
    def setUp(self):
        self.player_one = Player("Gosho", 50, 2, 16)
        self.player_two = Player("Misho", 50, 2, 16)

    #needs user input
    def test_choose_game_level(self):
        results = choose_game_level()
        keys, values = results[0].keys(), results[0].values()
        list_levels = list(keys)
        value_results = list(values)
        get_level_sizes = []
        for level_size in value_results:
            get_level_sizes.append(level_size[1])   
        assert list_levels == ['SMALL', 'MEDIUM', 'LARGE']
        assert get_level_sizes == [2, 3, 4]

    @mock.patch("InputOutput.random.randint", return_value = 5)
    def test_next_move(self, mock_randint):
        assert next_move(mock_randint) == 5

   
    def check_health(self):
        assert check_health(self.player_one, self.player_two) == True

        
if __name__ == '__main__':
    unittest.main()