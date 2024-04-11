import unittest

from figures.Circle import Circle
from figures.Triangle import Triangle


class FiguresTest(unittest.TestCase):

    def test_is_triangle_exist(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 5)
        with self.assertRaises(ValueError):
            Triangle(1, 2, -3)

        Triangle(2,3,4)
        Triangle(3,3,3)
        Triangle(2,3,3)

    def test_is_circle_exist(self):
        with self.assertRaises(ValueError):
            Circle(-4)
        Circle(0)
        Circle(5)

    def test_circle_square(self):
        circle_square = Circle(20).calculate_square()
        self.assertEqual(circle_square, 1256.64)

    def test_triangle_square(self):
        triangle_square = Triangle(2, 4, 3).calculate_square()
        self.assertEqual(triangle_square, 2.9)

    def test_triangle_is_right(self):
        triangle1 = Triangle(3, 4, 5)
        triangle2 = Triangle(70, 130, 110)
        self.assertEqual(triangle1.is_right(), True)
        self.assertEqual(triangle2.is_right(), False)
