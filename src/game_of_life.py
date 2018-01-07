class Game(object):
    def __init__(self, infile):
        self.infile = infile
        self.raw_input = file_helper(self.infile)
        self.grid = create_grid(self.raw_input)
        self.live_cells = live_cells(self.grid)

    def evolve(self):
        new_grid = set()
        for cell in self.grid:
            x, y, v = cell
            live_neighbors = list(set(self.live_cells) - set(cell_neighbors((x, y))))
            # living cell
            if v == "*":
                # living cell with less than 2 or more than 3 neighbors dies
                if len(live_neighbors) < 2 or live_neighbors > 3:
                    v = "."

            new_grid.add((x, y, v))
        self.grid = new_grid


def file_helper(infile):
    my_infile = open(infile, "r")
    lines = my_infile.readlines()
    my_infile.close()
    return lines


def parse_lines(lines):
    y = 0
    for l in lines:
        x = 0
        l = l.strip()
        for v in l:
            yield x, y, v
            x +=1
        y += 1


def create_grid(lines):
    grid = set()
    for c in parse_lines(lines):
        x, y, v = c
        grid.add((x, y, v))
    return grid


def live_cells(grid):
    return [(x[0], x[1]) for x in grid if x[2] == "*"]


def cell_neighbors(cell):
    offset = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    x, y = cell
    return [(x + ox, y + oy) for (ox, oy) in offset]






