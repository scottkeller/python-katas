"""Programming Kata for Conway's Game of Life
Meets all requirements of Kata at: http://codingdojo.org/kata/GameOfLife/"""


class Game(object):
    """Game of Life base class"""
    def __init__(self, infile):
        self.infile = infile
        self.raw_input = file_helper(self.infile)
        self.grid = create_grid(self.raw_input)
        self.live_cells = live_cells(self.grid)

    def show_grid(self):
        """prints the grid's text representation"""
        print grid_text(self.grid)
        print ""

    def evolve(self):
        """steps forward in evolution based on the rules of the game"""
        new_grid = set()
        for cell in self.grid:
            x, y, v = cell
            live_neighbors = list((set(self.live_cells)) & set(cell_neighbors((x, y))))
            # living cell
            if v == "*":
                # living cell with less than 2 or more than 3 neighbors dies
                if len(live_neighbors) < 2 or len(live_neighbors) > 3:
                    v = "."
                # dead cell spawns life with exactly 3 live neighbors
            if v == ".":
                if len(live_neighbors) == 3:
                    v = "*"
            new_grid.add((x, y, v))
        self.grid = new_grid
        self.live_cells = live_cells(self.grid)


def file_helper(infile):
    """reads a file in as lines"""
    my_infile = open(infile, "r")
    lines = my_infile.readlines()
    my_infile.close()
    return lines


def parse_lines(lines):
    """parses each line and returns the x,y coordinates
    and value of each character"""
    y = 0
    for l in lines:
        x = 0
        l = l.strip()
        for v in l:
            yield x, y, v
            x += 1
        y += 1


def create_grid(lines):
    """creates a grid from input lines"""
    grid = set()
    for c in parse_lines(lines):
        x, y, v = c
        grid.add((x, y, v))
    return grid


def live_cells(grid):
    """returns cells on a grid are alive"""
    return [(x[0], x[1]) for x in grid if x[2] == "*"]


def cell_neighbors(cell):
    """returns neighboring cell x,y coordinates"""
    offset = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    x, y = cell
    return [(x + ox, y + oy) for (ox, oy) in offset]


def grid_text(grid):
    """converts grid to text representation"""
    sorted_grid = sorted(list(grid), key=lambda k: (k[1], k[0]))
    text = ""
    prev_y = 0
    for cell in sorted_grid:
        x, y, v = cell
        if y > prev_y:
            text += "\n"
        text += v
        prev_y = y
    return text
