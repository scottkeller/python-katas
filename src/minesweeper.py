"""Programming Kata for Minesweeper game
Meets all requirements as described here: http://codingdojo.org/kata/Minesweeper/
EXCEPT: Dimensions are not included in file.
Program can hypothetically process an infinite size grid"""


class Game(object):
    """base game class"""
    def __init__(self, infile):
        self.infile = infile
        self.raw_input = file_helper(self.infile)


def file_helper(infile):
    """returns input file as list of lines"""
    with open(infile, "r") as my_file:
        lines = my_file.readlines()
    return lines
