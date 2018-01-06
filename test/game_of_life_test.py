import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.game_of_life import Game

class TestGameOfLife(unittest.TestCase):

    def test_create_game(self):
        game = Game(None)

    def test_read_input_file(self):
        infile = os.path.abspath("./game_of_life_test_input/one_live_cell.txt")
        game = Game(infile)
        assert game.infile == infile



if __name__ == '__main__':
    unittest.main()