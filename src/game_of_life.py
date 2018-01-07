class Game(object):
    def __init__(self, infile):
        self.infile = infile
        self.raw_input = file_helper(self.infile)


def file_helper(infile):
    my_infile = open(infile, "r")
    lines = my_infile.readlines()
    my_infile.close()
    return lines


