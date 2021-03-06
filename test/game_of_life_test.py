import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.game_of_life import Game


class TestGameOfLife(unittest.TestCase):

    def test_get_input_filename(self):
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/one_live_cell.txt')
        game = Game(infile)
        assert game.infile == infile

    def test_read_input_file(self):
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/one_live_cell.txt')
        game = Game(infile)
        assert game.raw_input[0] == '*'

    def test_grid_creation(self):
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/one_live_cell.txt')
        game = Game(infile)
        assert game.grid == set([(0, 0, '*')])

    def test_live_cells(self):
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/one_live_cell.txt')
        game = Game(infile)
        assert game.live_cells == [(0, 0)]

    def test_cell_neighbors_point_of_origin(self):
        from src.game_of_life import cell_neighbors
        neighbors = cell_neighbors((0, 0))
        assert neighbors == [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    def test_one_live_cell_death(self):
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/one_live_cell.txt')
        game = Game(infile)
        game.evolve()
        assert game.grid == set([(0, 0, '.')])

    def test_one_dead_cell_life(self):
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/one_dead_cell_life.txt')
        game = Game(infile)
        game.evolve()
        assert game.grid == set([(0, 0, '*'), (0, 1, '*'), (1, 0, '*'), (1, 1, '*')])

    def test_grid_text(self):
        from src.game_of_life import grid_text
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/one_dead_cell_life.txt')
        with open(infile, 'r') as my_file:
            file_text = my_file.read()
        game = Game(infile)
        assert file_text == grid_text(game.grid)

    def test_blinker(self):
        # blinker changes back and forth each evolution
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/blinker.txt')
        game = Game(infile)
        grid1 = set([(0, 0, '.'), (1, 0, '.'), (2, 0, '.'),
                     (0, 1, '*'), (1, 1, '*'), (2, 1, '*'),
                     (0, 2, '.'), (1, 2, '.'), (2, 2, '.')])

        grid2 = set([(0, 0, '.'), (1, 0, '*'), (2, 0, '.'),
                     (0, 1, '.'), (1, 1, '*'), (2, 1, '.'),
                     (0, 2, '.'), (1, 2, '*'), (2, 2, '.')])

        assert game.grid == grid1
        game.evolve()
        assert game.grid == grid2
        game.evolve()
        assert game.grid == grid1
        game.evolve()
        assert game.grid == grid2

    def test_boat(self):
        # boat is a stable pattern
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/boat.txt')
        game = Game(infile)
        temp_grid = game.grid
        for i in range(1000):
            game.evolve()
            assert game.grid == temp_grid

    def test_extinction(self):
        # pattern will end in extinction after 2 evolutions
        infile = os.path.join(os.path.dirname(__file__), 'game_of_life_test_input/extinction.txt')
        game = Game(infile)
        game.evolve()
        game.evolve()
        assert game.live_cells == []


if __name__ == '__main__':
    unittest.main()