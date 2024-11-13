import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
   def test_area_zero(self):
       self.assertRaises(Exception, lambda:area(10,0));
   def test_area_neg(self):
       self.assertRaises(Exception, lambda:area(10,-5));
   def test_area_square(self):
       res = area(10, 10)
       self.assertEqual(res, 100)
   def test_area_int_int(self):
       res = area(10, 2)
       self.assertEqual(res, 20)
   def test_area_square_double(self):
       res = area(2.5, 2.5)
       self.assertEqual(res, 6.25)
   def test_area_zero_double(self):
       self.assertRaises(Exception, lambda:area(0, 7.5));
   def test_area_double_zero(self):
       self.assertRaises(Exception, lambda:area(2.5, 0));
   def test_area_int_double(self):
       res = area(2, 7.5)
       self.assertEqual(res, 15)
   def test_area_double_int(self):
       res = area(2.5, 7)
       self.assertEqual(res, 17.5)
   def test_area_double_double(self):
       res = area(2.5, 7.5)
       self.assertEqual(res, 18.75)
   def test_area_big(self):
       res = area(2000000000000000000000000, 3000000000000000000000000)
       self.assertEqual(res, 6000000000000000000000000000000000000000000000000)


   def test_perimeter_square(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)
   def test_perimeter_neg(self):
       self.assertRaises(Exception, lambda:perimeter(10,-5));
   def test_perimeter_zero(self):
       self.assertRaises(Exception, lambda:perimeter(0, 10));
   def test_perimeter_int_int(self):
       res = perimeter(10, 2)
       self.assertEqual(res, 24)
   def test_perimeter_square_double(self):
       res = perimeter(2.5, 2.5)
       self.assertEqual(res, 10)
   def test_perimeter_int_double(self):
       res = perimeter(2, 7.5)
       self.assertEqual(res, 19)
   def test_perimeter_double_int(self):
       res = perimeter(2.5, 7)
       self.assertEqual(res, 19)
   def test_perimeter_double_double(self):
       res = perimeter(2.5, 7.5)
       self.assertEqual(res, 20)
   def test_perimeter_big(self):
       res = perimeter(2000000000000000000000000, 2000000000000000000000000)
       self.assertEqual(res, 8000000000000000000000000)
