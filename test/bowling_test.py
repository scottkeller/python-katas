import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.bowling import Game


class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_all_gutters(self):
        for n in range(20):
            self.game.bowl(0)
        assert self.game.score() == 0

    def test_all_ones(self):
        for n in range(20):
            self.game.bowl(1)
        assert self.game.score() == 20


if __name__ == '__main__':
    unittest.main()