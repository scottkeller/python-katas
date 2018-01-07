class Game(object):
    def __init__(self, infile):
        self.infile = infile
        self.raw_input = file_helper(self.infile)
        self.grid = create_grid(self.raw_input)


def file_helper(infile):
    my_infile = open(infile, "r")
    lines = my_infile.readlines()
    my_infile.close()
    return lines


def parse_lines(lines):
    x = 0
    y = 0
    for l in lines:
        for c in l:
            yield [x, y]
            x += 1
        y += 1


def create_grid(lines):
    grid = []
    for c in parse_lines(lines):
        grid.append(c)
    return grid






