import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.bowling import Game


class TestBowling(unittest.TestCase):

    def test_create_game(self):
        game = Game()


if __name__ == '__main__':
    unittest.main()
