#!/usr/bin/python3
"""Unittest Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Perfom tests
    """
    def test_1_id_base(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_2_id_base(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_3_100_id_base(self):
        for i in range(100):
            x = ("b" + str(i))
            x = Base()
        self.assertEqual(x.id, 103)

    def test_4_neg_id_base(self):
        n = Base(-1)
        self.assertEqual(n.id, -1)

    def test_5_arg_id_base(self):
        b1 = Base(999)
        b2 = Base(5)
        self.assertEqual(b1.id, 999)
        self.assertEqual(b2.id, 5)
