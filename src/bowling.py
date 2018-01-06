class Game():
    def __init__(self):
        self.throws = []

    def bowl(self, pins):
        self.throws.append(pins)

    def score(self):
        total = 0;
        for n in self.throws:
            total += n
        return total