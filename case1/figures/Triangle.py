import math

from case1.figures.IFigure import IFigure


class Triangle(IFigure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.is_valid()

    def is_valid(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
            return
        raise ValueError(f"The triangle doesn't exist with the given parameters: "
                         f"a={self.a} b={self.b} c={self.c}")

    def calculate_square(self):
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return round(s, 2)

    def is_right(self):
        a, b, c = sorted([self.a, self.b, self.c])
        return math.pow(c, 2) == math.pow(a, 2) + math.pow(b, 2)