import unittest
import pytest
import sys
sys.path.append("..")
from models.Cell import *
from models.CardFactory import *

class Test_Cell(unittest.TestCase):

    def test_initial_values_Cell(self):
        cards = [BadCard(), GoodCard(), TripCard()]
        obj_1 = Cell(1,2,cards)     
        assert obj_1.row == 1
        assert obj_1.col == 2
        assert obj_1.cards == cards

    def test_no_value(self):
        with pytest.raises(Exception) as e_info:
            obj = Cell()      

if __name__ == '__main__':
    unittest.main()        