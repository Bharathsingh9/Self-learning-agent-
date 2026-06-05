python
import unittest
from calculator import Calculator

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        with self.assertRaises(TypeError):
            self.calc.add(2, 'a')

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        with self.assertRaises(TypeError):
            self.calc.subtract(5, 'a')

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        with self.assertRaises(TypeError):
            self.calc.multiply(4, 'a')

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(6, 0)
        with self.assertRaises(TypeError):
            self.calc.divide(6, 'a')

    def test_square(self):
        self.assertEqual(self.calc.square(4), 16)
        with self.assertRaises(TypeError):
            self.calc.square('a')

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
        with self.assertRaises(TypeError):
            self.calc.square_root('a')

if __name__ == '__main__':
    unittest.main()



# calculator.py

class Calculator:
    def add(self, *args):
        if not all(isinstance(i, (int, float)) for i in args):
            raise TypeError('Input must be a number')
        return sum(args)

    def subtract(self, *args):
        if not all(isinstance(i, (int, float)) for i in args):
            raise TypeError('Input must be a number')
        if len(args) < 2:
            raise TypeError('Two arguments required')
        return args[0] - args[1]

    def multiply(self, *args):
        if not all(isinstance(i, (int, float)) for i in args):
            raise TypeError('Input must be a number')
        return args[0] * args[1]

    def divide(self, *args):
        if not all(isinstance(i, (int, float)) for i in args):
            raise TypeError('Input must be a number')
        if len(args) < 2:
            raise TypeError('Two arguments required')
        if args[1] == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return args[0] / args[1]

    def square(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError('Input must be a number')
        return num ** 2

    def square_root(self, num):
        if not isinstance(num, (int, float)):
            raise TypeError('Input must be a number')
        if num < 0:
            raise ValueError('Cannot calculate square root of a negative number')
        return num ** 0.5
