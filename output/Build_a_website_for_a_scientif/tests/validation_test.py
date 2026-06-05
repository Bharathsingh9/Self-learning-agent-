python
import unittest
from scientific_calculator import ScientificCalculator

class TestValidation(unittest.TestCase):

    def test_positive_number(self):
        calculator = ScientificCalculator()
        calculator.num1 = 5
        calculator.num2 = 5
        self.assertEqual(calculator.add(), 10)
        self.assertEqual(calculator.subtract(), 0)
        self.assertEqual(calculator.multiply(), 25)
        self.assertEqual(calculator.divide(), 1)

    def test_negative_number(self):
        calculator = ScientificCalculator()
        calculator.num1 = -5
        calculator.num2 = -5
        self.assertEqual(calculator.add(), -10)
        self.assertEqual(calculator.subtract(), 0)
        self.assertEqual(calculator.multiply(), 25)
        self.assertEqual(calculator.divide(), 1)

    def test_decimal_number(self):
        calculator = ScientificCalculator()
        calculator.num1 = 5.5
        calculator.num2 = 5.5
        self.assertEqual(calculator.add(), 11.0)
        self.assertEqual(calculator.subtract(), 0.0)
        self.assertEqual(calculator.multiply(), 30.25)
        self.assertEqual(calculator.divide(), 1.0)

    def test_large_number(self):
        calculator = ScientificCalculator()
        calculator.num1 = 1000000000
        calculator.num2 = 500000000
        self.assertEqual(calculator.add(), 1500000000)
        self.assertEqual(calculator.subtract(), 500000000)
        self.assertEqual(calculator.multiply(), 500000000000000)
        self.assertEqual(calculator.divide(), 2)

    def test_large_decimal_number(self):
        calculator = ScientificCalculator()
        calculator.num1 = 1000000000.5
        calculator.num2 = 500000000.5
        self.assertEqual(calculator.add(), 1500000001.0)
        self.assertEqual(calculator.subtract(), 500000000.0)
        self.assertEqual(calculator.multiply(), 500000000000000.25)
        self.assertEqual(calculator.divide(), 2.0)

    def test_zero_divisor(self):
        calculator = ScientificCalculator()
        with self.assertRaises(ZeroDivisionError):
            calculator.divide()
        calculator.num2 = 5
        with self.assertRaises(ZeroDivisionError):
            calculator.divide()

    def test_invalid_input_type(self):
        calculator = ScientificCalculator()
        with self.assertRaises(TypeError):
            calculator.num1 = 'a'
            calculator.num2 = 'b'
            calculator.add()
        with self.assertRaises(TypeError):
            calculator.num1 = 1
            calculator.num2 = 'b'
            calculator.add()

    def test_non_numeric_input(self):
        calculator = ScientificCalculator()
        with self.assertRaises(ValueError):
            calculator.num1 = 'a'
            calculator.add()
        with self.assertRaises(ValueError):
            calculator.num1 = 'a'
            calculator.subtract()
        with self.assertRaises(ValueError):
            calculator.num1 = 'a'
            calculator.multiply()
        with self.assertRaises(ValueError):
            calculator.num1 = 'a'
            calculator.divide()

if __name__ == '__main__':
    unittest.main()
