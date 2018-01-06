class Game():
    def __init__(self):
        self.throws = []
        self.throw_num = 0

    def bowl(self, pins):
        self.throws.append(pins)
        self.throw_num += 1

    def score(self):
        total = 0
        frames = 10
        frame_index = 0
        for n in range(frames):
            if self.is_spare(frame_index):
                total += self.score_spare(frame_index)
                frame_index += 2
            else:
                total += self.score_frame(frame_index)
                frame_index += 2
        return total

    def is_spare(self, frame_index):
        return self.throws[frame_index] + self.throws[frame_index + 1] == 10

    def score_frame(self, frame_index):
        return self.throws[frame_index] + self.throws[frame_index + 1]

    def score_spare(self, frame_index):
        return 10 + self.throws[frame_index + 2]