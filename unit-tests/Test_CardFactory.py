import unittest
import pytest
import sys
sys.path.append("..")
from models.CardFactory import *

class Test_CardFactory(unittest.TestCase):

    def test_initial_value_GoodCard(self):
        obj_1 = GoodCard()     
        assert obj_1.health_points == 50

    def test_initial_value_BadCard(self):
        obj_1 = BadCard()     
        assert obj_1.damage == 10

    def test_initial_TripCard(self):
        obj_1 = TripCard()
        assert type(obj_1) == TripCard      


if __name__ == '__main__':
    unittest.main()