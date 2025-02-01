import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(4, 3), 7)
        self.assertEqual(self.calc.add(-4, 3), -1)


    def test_division(self):
        self.assertEqual(self.calc.divide(4, 2), 2.0)
        self.assertRaises(ZeroDivisionError, self.calc.divide(4, 0))



    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 3), 1)


    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-4, -3), 12)


if __name__ == "__main__":
    unittest.main()