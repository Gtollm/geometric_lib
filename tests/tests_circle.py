import unittest
from math import pi
from circle import *

class CircleTestCase(unittest.TestCase):
   def test_area_zero(self):
       res = area(0)
       self.assertEqual(res, 0)
   def test_area_int(self):
       res = area(10)
       self.assertEqual(res, 100 * pi)
   def test_area_double(self):
       res = area(2.5)
       self.assertEqual(res, 6.25 * pi)
   def test_area_big(self):
       res = area(2000000000000000000000000)
       self.assertEqual(res, 4000000000000000000000000000000000000000000000000 * pi)

   def test_perimeter_zero(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
   def test_perimeter_int(self):
       res = perimeter(10)
       self.assertEqual(res, 20 * pi)
   def test_perimeter_double(self):
       res = perimeter(2.5)
       self.assertEqual(res, 5 * pi)
   def test_perimeter_big(self):
       res = perimeter(2000000000000000000000000)
       self.assertEqual(res, 4000000000000000000000000 * pi)
