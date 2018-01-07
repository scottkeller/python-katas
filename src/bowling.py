"""Programming Kata for Bowling Game problem
Meets all requirements of: http://codingdojo.org/kata/Bowling/"""


class Game(object):
    """Bowling game base class"""
    def __init__(self):
        self.throws = []
        self.throw_num = 0

    def bowl(self, pins):
        """Throw the ball"""
        self.throws.append(pins)
        self.throw_num += 1

    def score(self):
        """calculate the score"""
        total = 0
        frames = 10
        frame_index = 0
        for n in range(frames):
            if self.is_strike(frame_index):
                total += self.score_strike(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                total += self.score_spare(frame_index)
                frame_index += 2
            else:
                total += self.score_frame(frame_index)
                frame_index += 2
        return total

    def is_spare(self, frame_index):
        """checks if frame is a spare"""
        return self.throws[frame_index] + self.throws[frame_index + 1] == 10

    def is_strike(self, frame_index):
        """checks if frame is a strike"""
        return self.throws[frame_index] == 10

    def score_strike(self, frame_index):
        """returns score for a frame if a strike was scored"""
        return 10 + self.throws[frame_index + 1] + self.throws[frame_index + 2]

    def score_spare(self, frame_index):
        """returns score for a frame if no spare or strike was scored"""
        return 10 + self.throws[frame_index + 2]

    def score_frame(self, frame_index):
        """returns score for a frame if a spare was scored"""
        return self.throws[frame_index] + self.throws[frame_index + 1]
