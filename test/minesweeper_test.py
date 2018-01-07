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

    def test_hint_count(self):
        infile = os.path.abspath('./minesweeper_test_input/one_mine.txt')
        game = Game(infile)
        assert game.hint() == set([(0, 0, '*'), (1, 0, 1)])

    def test_grid_text(self):
        from src.minesweeper import grid_text
        infile = os.path.abspath("./minesweeper_test_input/4_4_grid_2_mines.txt")
        with open(infile, "r") as my_file:
            file_text = my_file.read()
        game = Game(infile)
        assert file_text == grid_text(game.grid)

    def test_4_4_grid_2_mines(self):
        infile = os.path.abspath('./minesweeper_test_input/4_4_grid_2_mines.txt')
        game = Game(infile)
        assert game.hint() == set([(0, 0, '*'), (1, 0, 1), (2, 0, 0), (3, 0, 0),
                                   (0, 1, 2), (1, 1, 2), (2, 1, 1), (3, 1, 0),
                                   (0, 2, 1), (1, 2, '*'), (2, 2, 1), (3, 2, 0),
                                   (0, 3, 1), (1, 3, 1), (2, 3, 1), (3, 3, 0)])

    def test_3_5_grid_3_mines(self):
        infile = os.path.abspath('./minesweeper_test_input/3_5_grid_3_mines.txt')
        game = Game(infile)
        assert game.hint() == set([(0, 0, '*'), (1, 0, '*'), (2, 0, 1), (3, 0, 0), (4, 0, 0),
                                   (0, 1, 3), (1, 1, 3), (2, 1, 2), (3, 1, 0), (4, 1, 0),
                                   (0, 2, 1), (1, 2, '*'), (2, 2, 1), (3, 2, 0), (4, 2, 0)])

    def test_show_grid(self):
        infile = os.path.abspath('./minesweeper_test_input/4_4_grid_2_mines.txt')
        game = Game(infile)
        game.show_grid()
        game.show_hint()
        infile = os.path.abspath('./minesweeper_test_input/3_5_grid_3_mines.txt')
        game = Game(infile)
        game.show_grid()
        game.show_hint()

if __name__ == '__main__':
    unittest.main()