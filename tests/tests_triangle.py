import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
   def test_area_zero(self):
       self.assertRaises(Exception, lambda:area(10, 0));
   def test_area_zero_neg(self):
       self.assertRaises(Exception, lambda:area(-10, -10));
   def test_area_square(self):
       res = area(10, 10)
       self.assertEqual(res, 50)
   def test_area_int_int(self):
       res = area(10, 2)
       self.assertEqual(res, 10)
   def test_area_square_double(self):
       res = area(2.5, 2.5)
       self.assertEqual(res, 3.125)
   def test_area_zero_double(self):
       self.assertRaises(Exception, lambda:area(0, 7.5));
   def test_area_double_zero(self):
       self.assertRaises(Exception, lambda:area(2.5, 0));
   def test_area_int_double(self):
       res = area(2, 7.5)
       self.assertEqual(res, 7.5)
   def test_area_double_int(self):
       res = area(2.5, 7)
       self.assertEqual(res, 8.75)
   def test_area_double_double(self):
       res = area(2.5, 7.5)
       self.assertEqual(res, 9.375)
   def test_area_big(self):
       res = area(2000000000000000000000, 2000000000000000000000)
       self.assertEqual(res, 2000000000000000000000000000000000000000000.0)

   def test_perimeter_neg(self):
       self.assertRaises(Exception, lambda:area(-10, -10));
   def test_perimeter_zero(self):
       self.assertRaises(Exception, lambda:perimeter(10, 0, 7));
   def test_perimeter_int_int_int(self):
       res = perimeter(10, 11, 12)
       self.assertEqual(res, 33)
   def test_perimeter_int_int_double(self):
       self.assertRaises(Exception, lambda:perimeter(10, 2, 2.5));
   def test_perimeter_int_double_int(self):
       res = perimeter(2, 2.5, 3)
       self.assertEqual(res, 7.5)
   def test_perimeter_double_int_int(self):
       res = perimeter(2.5, 3,4)
       self.assertEqual(res, 9.5)
   def test_perimeter_int_double_double(self):
       res = perimeter(2, 2.5, 3.5)
       self.assertEqual(res, 8)
   def test_perimeter_double_double_int(self):
       res = perimeter(2.5, 3.5, 4)
       self.assertEqual(res, 10)
   def test_perimeter_double_int_double(self):
       res = perimeter(2.5, 6, 3.5)
       self.assertEqual(res, 12)
   def test_perimeter_double_double_double(self):
       self.assertRaises(Exception, lambda:perimeter(2.5, 6.5, 3.5));
   def test_perimeter_big(self):
       res = perimeter(2000000000000000000000000, 3000000000000000000000000, 4000000000000000000000000)
       self.assertEqual(res, 9000000000000000000000000)
