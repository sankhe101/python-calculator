"""Run with: python -m unittest -v."""

import unittest
from decimal import Decimal

from calculator import add_numbers


class AdditionTests(unittest.TestCase):
    def test_decimal_addition_is_exact(self):
        self.assertEqual(add_numbers("0.1", "0.2"), Decimal("0.3"))

    def test_negative_number(self):
        self.assertEqual(add_numbers("-5", "2"), Decimal("-3"))


if __name__ == "__main__":
    unittest.main()
