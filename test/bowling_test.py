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
        self.bowl_multi(0, 20)
        assert self.game.score() == 0

    def test_all_ones(self):
        self.bowl_multi(1, 20)
        assert self.game.score() == 20

    def test_first_spare(self):
        self.game.bowl(1)
        self.game.bowl(9)
        self.bowl_multi(1, 18)
        assert self.game.score() == 29

    def test_first_strike(self):
        self.game.bowl(10)
        self.bowl_multi(2, 18)
        assert self.game.score() == 50

    def test_tenth_frame_spare(self):
        self.bowl_multi(0, 19)
        self.game.bowl(10)
        self.bowl_multi(1, 1)
        assert self.game.score() == 11

    def bowl_multi(self, pins, throws):
        for n in range(throws):
            self.game.bowl(pins)

if __name__ == '__main__':
    unittest.main()