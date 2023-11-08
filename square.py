import unittest


def area(a):
    """Принимает число a (сторона квадрата), возвращает площадь  квадрата"""
    return a * a


def perimeter(a):
    """Принимает число a (сторона квадрата), возвращает периметр квадрата"""
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        result = area(5)
        self.assertEqual(result, 25)

    def test_square_mul(self):
        result = perimeter(6)
        self.assertEqual(result, 24)

