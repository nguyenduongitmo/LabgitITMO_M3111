import math
import unittest


def area(r):
    """Принимает число r (радиус круга), возвращает площадь круга"""
    return math.pi * r * r


def perimeter(r):
    """Принимает число r (радиус круга), возвращает периметр круга"""
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_one_mul(self):
        result = area(3)
        self.assertEqual(result, 28.27433388)

    def test_two_mul(self):
        result = perimiter(1)
        self.assertEqual(result, 6.283185307)
