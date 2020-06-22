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
    return diagonal_1*diagonal_2/2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (base_minor+base_major)*height/2


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return perimeter*apothem/2


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    pi = math.pi
    return pi*(radius**2)


if __name__ == '__main__':
    import unittest
    import numpy

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

            for r in range(len(rectangle_areas)):
                t_base = test_base[r]
                t_height = test_height[r]
                answer = rectangle_areas[r]

                self.assertEqual(answer, rectangle_area(t_base, t_height))
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
            rhombus_areas = [7, 12, 18, 25, 33]
            for r in range(len(test_base)):
                t_base = test_base[r]
                t_height = test_height[r]
                answer = rhombus_areas[r]

                self.assertEqual(answer, triangle_area(t_base,t_height))

        def test_trapezoid_area(self):
            # Make this test first...
            Minor_base = [2, 3, 4, 5, 6]
            Major_Base = [4, 6, 6, 8, 12]
            trapezoid_heigth = [8, 7, 6, 5, 4]

            trapezoid_answer = [24, 31.5, 30, 32.5, 36]

            for r in range(len(trapezoid_answer)):
                Min_base = Minor_base[r]
                Maj_base = Major_Base[r]
                height = trapezoid_heigth[r]

                answer = trapezoid_answer[r]

                self.assertEqual(answer, trapezoid_area(Min_base, Maj_base, height))

        def test_regular_polygon_area(self):
            # Make this test first...
            perimeters_array = [18, 60, 40, 64, 60]
            apothems_array = [2.6, 8.66, 3, 6, 9.3]
            Area_RegPol_array = [23.4, 259.8, 60, 192, 279]

            for r in range(len(Area_RegPol_array)):
                perimeter = perimeters_array[r]
                apothem = apothems_array[r]
                answer = Area_RegPol_array[r]
                
                #DON'T ADD ARRAYS BECAUSE OF THE FLOAT VARIABLE TYPES
                self.assertAlmostEqual(answer, regular_polygon_area(perimeter, apothem)) 

        def test_circumference_area(self):
            
            # Make this test first...
            radius_array = [3, 7.33, 5, 8.6543, 9]
            circumference_answers_array = [28.27, 168.79, 78.54, 235.3, 254.47]

            for r in range(len(circumference_answers_array)):
                radius = radius_array[r]
                answer = circumference_answers_array[r]

                #DON'T ADD ARRAYS BECAUSE OF THE FLOAT VARIABLE TYPES
                self.assertAlmostEqual(answer, round(circumference_area(radius),2)) 

        def tearDown(self):
            # Delete the needed values for the tests
            # del(self.example_square_areas)
            del(self.squares_sides)

    unittest.main()
