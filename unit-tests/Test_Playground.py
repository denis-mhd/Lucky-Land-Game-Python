import unittest, mock
import pytest
import sys
sys.path.append("..")
from models.Playground import *
from models.Cell import Cell

class Test_Playground(unittest.TestCase):

    def setUp(self):
        self.obj_1 = Playground(5) 

    def test_initial_Playground(self): 
        assert self.obj_1.size == 5

    def test_no_value(self):
        with pytest.raises(Exception) as e_info:
            obj = Playground()     

    def test_build_playground(self):
        field = self.obj_1.build_playground()
        assert list(field[1][1])[0] == 7

if __name__ == '__main__':
    unittest.main()            