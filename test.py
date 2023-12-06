import unittest
import triangle
import square
import rectangle
import circle

class TriangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        assert triangle.area_triangle(7,8) == 28

    def test_one_mul(self):
        assert triangle.area_triangle(10, 5) == 25


    def test_two_mul(self):
        assert triangle.area_triangle(7.5, 3.5) == 13.125


    def test_three_mul(self):
        assert triangle.perimeter_triangle(0, 0,0) == 0


    def test_four_mul(self):
        assert triangle.perimeter_triangle(10, 4, 8) == 22


    def test_five_mul(self):
        assert triangle.perimeter_triangle(34.23, 42.34, 23.43) == 100


class SquareTestCase(unittest.TestCase):

    def test_zero_mul(self):
        assert square.area_square(0) == 0

    def test_one_mul(self):
        assert square.area_square(10) == 100

    def test_two_mul(self):
        assert square.area_square(7.5) == 56.25

    def test_three_mul(self):
        assert square.perimeter_square(0) == 0

    def test_four_mul(self):
        assert square.perimeter_square(10) == 40

    def test_five_mul(self):
        assert square.perimeter_square(17.25) == 69



class RectangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        assert rectangle.area_rectangle(0,13) == 0

    def test_one_mul(self):
        assert rectangle.area_rectangle(10,13) == 130

    def test_two_mul(self):
        assert rectangle.area_rectangle(67.5, 3.5) == 236.25


    def test_three_mul(self):
        assert rectangle.perimeter_rectangle(0,0) == 0


    def test_four_mul(self):
        assert rectangle.perimeter_rectangle(10, 54) == 128

    def test_five_mul(self):
        assert rectangle.perimeter_rectangle(67.636, 42.364) == 220


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        assert circle.area_circle(0) == 0

    def test_one_mul(self):
        assert circle.area_circle(10) == 314.1592653589793

    def test_two_mul(self):
        assert circle.area_circle(67.636) == 14371.619275936122

    def test_three_mul(self):
        assert circle.perimeter_circle(0) == 0

    def test_four_mul(self):
        assert circle.perimeter_circle(10) == 62.83185307179586

    def test_five_mul(self):
        assert circle.perimeter_circle(67.636) == 424.96952143639845