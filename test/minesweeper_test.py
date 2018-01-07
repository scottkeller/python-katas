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

    def test_get_raw_input(self):
        infile = os.path.abspath('./minesweeper_test_input/one_field.txt')
        game = Game(infile)
        assert game.raw_input == ["."]

    def test_grid_creation(self):
        infile = os.path.abspath('./minesweeper_test_input/one_field.txt')
        game = Game(infile)
        assert game.grid == set([(0, 0, ".")])

    def test_mines(self):
        infile = os.path.abspath('./minesweeper_test_input/one_mine.txt')
        game = Game(infile)
        assert game.mines == [(0, 0)]

    def test_cell_neighbors(self):
        from src.minesweeper import cell_neighbors
        neighbors = cell_neighbors((0, 0))
        assert neighbors == [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

if __name__ == '__main__':
    unittest.main()