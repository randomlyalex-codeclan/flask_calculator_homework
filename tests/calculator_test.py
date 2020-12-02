import unittest
from modules.calculator import Calculator

class TestCalculator(unittest.TestCase):
    

    def test_add(self):
        self.assertEqual(5, add(2,3))
    
    def test_subtract(self):
        self.assertEqual(5, subtract(10,5))

    def test_multiply(self):
        self.assertEqual(8, multiply(2,4))

    def test_divide(self):
        self.assertEqual(10, divide(20,2))