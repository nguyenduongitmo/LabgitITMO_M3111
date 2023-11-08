import unittest


def area(a, b):
    """Принимает число a и b (длина и ширина прямоугольника), возвращает площадь  прямоугольника"""
    return a * b 


def perimeter(a, b): 
    """Принимает число a и b (длина и ширина прямоугольника), возвращает периметр прямоугольника"""
    return (a + b)*2


class RectangleTestCase(unittest.TestCase):
    def test_rectangle1(self):
        result = area(2, 3)
        self.assertEqual(result, 6)

    def test_retangle2(self):
        result = perimeter(4, 8)
        self.assertEqual(result,  24)

if __name__ == '__main__':
    unittest.main()
