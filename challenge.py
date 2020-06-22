import math


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!
    return side**2


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return base*height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return base*height/2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    pass


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    pass


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    pass


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    pass


if __name__ == '__main__':
    import unittest
    test_base = [2, 3, 4, 5, 6]
    test_height = [7, 8, 9, 10, 11]
    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.squares_sides = {
                2: 4,
                3: 9,
                4: 16,
                5: 25,
                6: 36
            }

        def test_square_area(self):
            for key, value in self.squares_sides.items():
                self.assertEqual(value, square_area(key))

        def test_rectangle_area(self):
            # Make this test first...
            
            rectangle_areas = [14, 24, 36, 50, 66]
            for r in range(len(test_base)):
                t_base = test_base[r]
                t_height = test_height[r]
                answer = rectangle_areas[r]

                self.assertEqual(answer, rectangle_area(t_base,t_height))
            # pass

        def test_triangle_area(self):
            # Make this test first...
            
            triangle_areas = [7, 12, 18, 25, 33]
            for r in range(len(test_base)):
                t_base = test_base[r]
                t_height = test_height[r]
                answer = triangle_areas[r]

                self.assertEqual(answer, triangle_area(t_base,t_height))

        def test_rhombus_area(self):
            # Make this test first...
            pass

        def test_trapezoid_area(self):
            # Make this test first...
            pass

        def test_regular_polygon_area(self):
            # Make this test first...
            pass

        def test_circumference_area(self):
            # Make this test first...
            pass

        def tearDown(self):
            # Delete the needed values for the tests
            # del(self.example_square_areas)
            pass

    unittest.main()
