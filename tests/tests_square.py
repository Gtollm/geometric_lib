import unittest
from square import *

class SquareTestCase(unittest.TestCase):
   def test_area_zero(self):
       res = area(0)
       self.assertEqual(res, 0)
   def test_area_int(self):
       res = area(10)
       self.assertEqual(res, 100)
   def test_area_double(self):
       res = area(2.5)
       self.assertEqual(res, 6.25)
   def test_area_big(self):
       res = area(2000000000000000000000000)
       self.assertEqual(res, 4000000000000000000000000000000000000000000000000)

   def test_perimeter_zero(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
   def test_perimeter_int(self):
       res = perimeter(10)
       self.assertEqual(res, 40)
   def test_perimeter_double(self):
       res = perimeter(2.5)
       self.assertEqual(res, 10)
   def test_perimeter_big(self):
       res = perimeter(2000000000000000000000000)
       self.assertEqual(res, 8000000000000000000000000)


