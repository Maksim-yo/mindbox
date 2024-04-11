import math

from case1.figures.IFigure import IFigure


class Circle(IFigure):

    def __init__(self, r):
        self.r = r
        self.is_valid()

    def is_valid(self):
        if self.r >= 0:
            return
        raise ValueError(f"The circle doesn't exist with the given parameters: r={self.r}")

    def calculate_square(self):
        s = math.pi * math.pow(self.r, 2)
        return round(s, 2)