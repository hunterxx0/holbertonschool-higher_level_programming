#!/usr/bin/python3
"""Unittest Square
"""
import unittest
from models.square import Square


class TestRec(unittest.TestCase):
    """
    Perfom tests
    """
    def test_size_err_square(self):
        self.assertRaises(TypeError, Square, "0")
        self.assertRaises(TypeError, Square, True)
        self.assertRaises(TypeError, Square, 0.5)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)

    def test_square(self):
        b1 = Square(2, 4, 5, 100)
        b2 = Square(6, 10, 10, 5)
        self.assertEqual(b1.id, 100)
        self.assertEqual(b1.x, 4)
        self.assertEqual(b1.y, 5)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.size, 2)
        self.assertEqual(b1.area(), 4)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b2.x, 10)
        self.assertEqual(b2.y, 10)
        self.assertEqual(b2.width, 6)
        self.assertEqual(b2.height, 6)
        self.assertEqual(b2.size, 6)
        self.assertEqual(b2.area(), 36)

    def test_x_y_err_square(self):
        self.assertRaises(TypeError, Square, 1, 2, "x", 5)
        self.assertRaises(TypeError, Square, 1, "y", 3, 5)
        self.assertRaises(TypeError, Square, 2, 1, True, 5)
        self.assertRaises(TypeError, Square, 1, True, 3, 5)
        self.assertRaises(TypeError, Square, 1, 2, 1.5, 5)
        self.assertRaises(TypeError, Square, 1, 1.5, 3, 5)
        self.assertRaises(ValueError, Square, 1, 2, -1, 5)
        self.assertRaises(ValueError, Square, 1, -1, 2, 5)

    def test_update_square(self):
        b1 = Square(2, 4, 5, 100)
        b1.update(99, 98, 97, 96)
        self.assertEqual(b1.id, 99)
        self.assertEqual(b1.x, 97)
        self.assertEqual(b1.y, 96)
        self.assertEqual(b1.size, 98)
        self.assertEqual(b1.area(), 9604)
        b1.update(1000, x=1, y=1)
        self.assertEqual(b1.id, 1000)
        self.assertEqual(b1.x, 97)
        self.assertEqual(b1.y, 96)
        b1.update(size=1, y=1)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.size, 1)
        self.assertEqual(b1.y, 1)

    def test_update_err_square(self):
        b1 = Square(2, 4, 5, 100)
        self.assertRaises(TypeError, b1.update, 1, "s")
        self.assertRaises(TypeError, b1.update, 1, 2, True)
        self.assertRaises(TypeError, b1.update, 1, 2, 3, 1.5)
        self.assertRaises(TypeError, b1.update, 1, 2, 3, [1, 2])
        self.assertRaises(ValueError, b1.update, 1, 0)
        self.assertRaises(ValueError, b1.update, 1, 2, -1)
        self.assertRaises(ValueError, b1.update, 1, 2, 3, -100)
