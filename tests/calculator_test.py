import unittest
from modules.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5, Calculator.add_two_numbers(2,3))
    
    def test_subtract(self):
        self.assertEqual(5, Calculator.subtract_two_numbers(10,5))

    def test_multiply(self):
        self.assertEqual(8, Calculator.multiply_two_numbers(2,4))

    def test_divide(self):
        self.assertEqual(10, Calculator.divide_two_numbers(20,2))