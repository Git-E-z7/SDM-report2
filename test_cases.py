#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

#add
        def test_valid_minmin(self):
                self.assertEqual(1, calc(1, 1))

        def test_valid_maxmax(self):
                self.assertEqual(999*999, calc(999, 999))

        def test_valid_order_irrelevant(self):
                self.assertEqual(999, calc(999, 1))

        # --- Invalid equivalence class: non-int types (float / str) ---
        def test_invalid_float(self):
                self.assertEqual(-1, calc(1.0, 2))

        def test_invalid_numeric_string(self):
                self.assertEqual(-1, calc("3", 7))

        # --- Invalid equivalence class: malformed numeric strings that should not crash ---
        def test_invalid_mixed_string_should_not_crash(self):
                self.assertEqual(-1, calc("3a", 2))

        def test_invalid_one_numeric_one_alpha_should_not_crash(self):
                self.assertEqual(-1, calc("3", "b"))

