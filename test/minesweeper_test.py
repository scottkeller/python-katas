import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.minesweeper import Game


class TestMinesweeper(unittest.TestCase):
    def test_get_input_filename(self):
        infile = os.path.abspath('./minesweeper_test_input/one_field.txt')
        game = Game(infile)
        game.infile = infile

if __name__ == '__main__':
    unittest.main()