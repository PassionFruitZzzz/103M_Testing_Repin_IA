import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleFunction(unittest.TestCase):
    
    # ---------- Позитивные тесты ----------
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(6, 6, 6), "equilateral")
        self.assertEqual(get_triangle_type(0.5, 0.5, 0.5), "equilateral")
    
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(5, 5, 3), "isosceles")
        self.assertEqual(get_triangle_type(7, 4, 7), "isosceles")
        self.assertEqual(get_triangle_type(3.2, 4.0, 3.2), "isosceles")
    
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
        self.assertEqual(get_triangle_type(8, 9, 10), "nonequilateral")
        self.assertEqual(get_triangle_type(1.5, 2.0, 2.5), "nonequilateral")
    
    # ---------- Негативные тесты ----------
    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 5, 5)
    
    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 5, 5)
    
    def test_violates_inequality_1(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 5)
    
    def test_violates_inequality_2(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(4, 4, 8)
    
    def test_invalid_type(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("10", 10, 10)
    
    def test_invalid_type_float_str(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5.5, "6", 5.5)

if __name__ == "__main__":
    unittest.main()