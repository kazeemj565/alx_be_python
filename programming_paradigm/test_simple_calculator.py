import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(4, 3), 7)
        self.assertEqual(self.calc.add(-4, 3), -1)


    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2.0)
        self.assertRaises(ZeroDivisionError, self.calc.divide(4, 0))



    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 3), 1)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-4, -3), 12)


if __name__ == "__main__":
    unittest.main()