#!/usr/bin/python3
"""Unittest Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRec(unittest.TestCase):
    """
    Perfom tests
    """
    def test_width_str_rectangle(self):
        self.assertRaises(TypeError, Rectangle, "0", 1)

    def test_height_str_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, "1")

    def test_width_bool_rectangle(self):
        self.assertRaises(TypeError, Rectangle, True, 1)

    def test_height_bool_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, True)

    def test_width_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 0.5, 1)

    def test_height_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 1.5)

    def test_width_0_rectangle(self):
        self.assertRaises(ValueError, Rectangle, 0, 1)

    def test_height_0_rectangle(self):
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def test_width_neg_rectangle(self):
        self.assertRaises(ValueError, Rectangle, 1, -1)

    def test_height_neg_rectangle(self):
        self.assertRaises(ValueError, Rectangle, -1, 1)

    def test_width_list_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, [1, 2])

    def test_height_list_rectangle(self):
        self.assertRaises(TypeError, Rectangle, [1, 2], 1)

    def test_width_dict_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, {"1": 2})

    def test_height_dict_rectangle(self):
        self.assertRaises(TypeError, Rectangle, {"1": 2}, 1)

    def test_width_neg_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, (1,))

    def test_height_neg_rectangle(self):
        self.assertRaises(TypeError, Rectangle, (1,), 1)

    def test_rectangle(self):
        b1 = Rectangle(1, 2, 4, 5, 100)
        b2 = Rectangle(5, 6, 10, 10, 5)
        self.assertEqual(b1.id, 100)
        self.assertEqual(b1.x, 4)
        self.assertEqual(b1.y, 5)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.area(), 2)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b2.x, 10)
        self.assertEqual(b2.y, 10)
        self.assertEqual(b2.width, 5)
        self.assertEqual(b2.height, 6)
        self.assertEqual(b2.area(), 30)

    def test_x_str_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, "x", 5)

    def test_y_str_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 5, "y")

    def test_x_bool_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 2, 1, True, 5)

    def test_y_bool_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 5, True)

    def test_x_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 1.5, 5)

    def test_y_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 5, 1.5)

    def test_x_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, (1,), 5)

    def test_y_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 5, (1,))

    def test_x_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, [1, 2], 5)

    def test_y_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 5, [1, 2])

    def test_x_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, {"1": 5}, 5)

    def test_y_float_rectangle(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 5, {"1": 5})

    def test_x_neg_rectangle(self):
        self.assertRaises(ValueError, Rectangle, 1, 2, -1, 5)

    def test_y_neg_rectangle(self):
        self.assertRaises(ValueError, Rectangle, 1, 2, 5, -1)

    def test_update_rectangle(self):
        b1 = Rectangle(1, 2, 4, 5, 100)
        b2 = Rectangle(5, 6, 10, 10, 5)
        b1.update(99, 98, 97, 96, 95)
        self.assertEqual(b1.id, 99)
        self.assertEqual(b1.x, 96)
        self.assertEqual(b1.y, 95)
        self.assertEqual(b1.width, 98)
        self.assertEqual(b1.height, 97)
        self.assertEqual(b1.area(), 9506)
        b1.update(1000, x=1, y=1)
        self.assertEqual(b1.id, 1000)
        self.assertEqual(b1.x, 96)
        self.assertEqual(b1.y, 95)
        b1.update(x=1, y=1)
        self.assertEqual(b1.x, 1)
        self.assertEqual(b1.y, 1)

    def test_update_err_rectangle(self):
        b1 = Rectangle(1, 2, 4, 5, 100)
        self.assertRaises(TypeError, b1.update, 1, "s")
        self.assertRaises(TypeError, b1.update, 1, 2, True)
        self.assertRaises(TypeError, b1.update, 1, 2, 3, 1.5)
        self.assertRaises(TypeError, b1.update, 1, 2, 3, 4, [1, 2])
        self.assertRaises(ValueError, b1.update, 1, 0)
        self.assertRaises(ValueError, b1.update, 1, 2, -1)
        self.assertRaises(ValueError, b1.update, 1, 2, 3, -100)
        self.assertRaises(ValueError, b1.update, 1, 2, 3, 4, -99)
