import unittest


def area(a, h):
    """Принимает число a, h (основание и высота треугольника) возвращает площадь треугольника"""
    return a * h / 2


def perimeter(a, b, c):
    """Принимает число a, b, c (стороны треугольника), возвращает периметр треугольника"""
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        result = area(3, 4)
        self.assertEqual(result, 6, "Expected result to be 6")

    def test_one_mul(self):
        result = area(5, 6)
        self.assertEqual(result, 15)

    def test_two_mul(self):
        result = perimeter(3, 4, 5)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
