import unittest
from main import *


class TestMath(unittest.TestCase):

    def test_add(self) -> None:
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(2, 3), 6)

    def test_divide(self) -> None:
        self.assertEqual(divide(2, 2), 1)
        self.assertEqual(divide(2, 3), 2/3)
        self.assertRaises(ValueError, divide, 7, 0)
        self.assertRaises(NameError, divide, 7, 0)

    def test_modulo(self):
        self.assertEqual(modulo(2, 2), 0)
        self.assertEqual(modulo(2, 3), 2)
        self.assertRaises(ValueError, divide, 3, 0)
        self.assertRaises(TypeError, divide, 3, 0)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(4, 3), 11)

    def test_substract(self) -> None:
        self.assertEqual(substract(2, 2), 0)
        self.assertEqual(substract(2, 3), 1)


if __name__ == '__main__':
    unittest.main()