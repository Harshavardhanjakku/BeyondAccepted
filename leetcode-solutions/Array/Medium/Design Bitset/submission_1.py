# Problem: Design Bitset
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Bitset(object):

    def __init__(self, size):
        self.bs = [0] * size
        self.ones = 0
        self.n = size
        self.flipped = False

    def fix(self, idx):
        if not self.flipped:
            if self.bs[idx] == 0:
                self.bs[idx] = 1
                self.ones += 1
        else:
            if self.bs[idx] == 1:
                self.bs[idx] = 0
                self.ones += 1

    def unfix(self, idx):
        if not self.flipped:
            if self.bs[idx] == 1:
                self.bs[idx] = 0
                self.ones -= 1
        else:
            if self.bs[idx] == 0:
                self.bs[idx] = 1
                self.ones -= 1

    def flip(self):
        self.flipped = not self.flipped
        self.ones = self.n - self.ones

    def all(self):
        return self.ones == self.n

    def one(self):
        return self.ones > 0

    def count(self):
        return self.ones

    def toString(self):
        if not self.flipped:
            return "".join(map(str, self.bs))
        else:
            return "".join(str(1 - x) for x in self.bs)
