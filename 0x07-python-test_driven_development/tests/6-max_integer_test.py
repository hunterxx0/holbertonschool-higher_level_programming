#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Perfom tests
    """
    def tests_max_end(self):
        """
        Tests fuction's output when the max number is the last
        """
        self.assertEqual(max_integer([1, 5, 10]), 10)

    def tests_max_mid(self):
        """
        Tests fuction's output when the max number is the last
        """
        self.assertEqual(max_integer([1, 10, 5]), 10)

    def tests_max_zero(self):
        """
        Tests fuction's output with negative and zero
        """
        self.assertEqual(max_integer([0, -1, -5]), 0)

    def tests_max_empty(self):
        """
        Tests fuction's output with empty list
        """
        self.assertEqual(max_integer([]), None)

    def tests_max_one(self):
        """
        Tests fuction's output with one element in list
        """
        self.assertEqual(max_integer([2]), 2)

    def tests_max_same(self):
        """
        Tests fuction's output with equal elements in list
        """
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def tests_max_str(self):
        """
        Tests fuction's output with a string
        """
        self.assertEqual(max_integer("abc"), 'c')

    def tests_max_number(self):
        """
        Tests fuction's output with one number
        """
        self.assertRaises(TypeError, max_integer, 1)

    def tests_max_mixed(self):
        """
        Tests fuction's output with mixed types in list
        """
        self.assertRaises(TypeError, max_integer, [1, 'A', 5])

    def tests_max_none(self):
        """
        Tests fuction's output with empty list
        """
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
