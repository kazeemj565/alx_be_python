import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def test_add(self):
        calculator = SimpleCalculator()
        result = calculator.add(4, 3)
        self.assertEqual(result, 7)


    def test_divide(self):
        calculator = SimpleCalculator()
        result = calculator.divide(4, 2)
        self.assertEqual(result, 2.0)




    def test_subtract(self):
        calculator = SimpleCalculator()
        result = calculator.subtract(4, 3)
        self.assertEqual(result, 1)


    def test_multiply(self):
        calculator = SimpleCalculator()
        result = calculator.multiply(4, 3)
        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()