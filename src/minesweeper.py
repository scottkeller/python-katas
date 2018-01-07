"""Programming Kata for Minesweeper game
Meets all requirements as described here: http://codingdojo.org/kata/Minesweeper/
EXCEPT: Dimensions are not included in file.
Program can hypothetically process an infinite size grid"""


class Game(object):
    """base game class"""
    def __init__(self, infile):
        self.infile = infile
        self.raw_input = file_helper(self.infile)
        self.grid = create_grid(self.raw_input)
        self.mines = find_mines(self.grid)


def file_helper(infile):
    """returns input file as list of lines"""
    with open(infile, "r") as my_file:
        lines = my_file.readlines()
    return lines


def parse_lines(lines):
    """returns x,y coordinates and value of cells"""
    y = 0
    for l in lines:
        x = 0
        l = l.strip()
        for v in l:
            yield x, y, v
            x += 1
        y += 1


def create_grid(lines):
    """creates a a grid from input lines"""
    grid = set()
    for c in parse_lines(lines):
        x, y, v = c
        grid.add((x, y, v))
    return grid


def find_mines(grid):
    """finds the x,y coordinates of mines in the grid"""
    return [(x[0], x[1]) for x in grid if x[2] == '*']


def cell_neighbors(cell):
    """finds the neighboring cells"""
    offset = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    x, y = cell
    return [(x + ox, y + oy) for (ox, oy) in offset]
