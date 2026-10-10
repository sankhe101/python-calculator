"""Run with: python -m unittest -v."""

import unittest
from decimal import Decimal

from calculator import CalculationError, add_numbers, calculate, format_result


class AdditionTests(unittest.TestCase):
    def test_decimal_addition_is_exact(self):
        self.assertEqual(add_numbers("0.1", "0.2"), Decimal("0.3"))

    def test_negative_number(self):
        self.assertEqual(add_numbers("-5", "2"), Decimal("-3"))


class ExpressionTests(unittest.TestCase):
    def test_prd_examples_and_precedence(self):
        examples = {
            "2 + 3 × 4": "14", "(2 + 3) × 4": "20", "-5 + 2": "-3",
            "0.1 + 0.2": "0.3", "50%": "0.5", "200 × 10%": "20",
            "200 + 10%": "200.1", "8 / 4 / 2": "1", "5 - 2 - 1": "2",
            "2 * -3": "-6", "-(2 + 3)": "-5", ".5 + .25": "0.75",
            "(20 + 30)%": "0.5", "1e-7 * 10": "0.000001",
        }
        for expression, expected in examples.items():
            with self.subTest(expression=expression):
                self.assertEqual(format_result(calculate(expression)), expected)

    def test_invalid_expressions_are_rejected(self):
        for expression in ("", "2+", "(2+3", "2 3", "2(3)", "2**3", "3//2",
                           "__import__('os')", "NaN", "1..2", ")", "2%3", "a"):
            with self.subTest(expression=expression):
                with self.assertRaises(CalculationError):
                    calculate(expression)

    def test_zero_division(self):
        with self.assertRaisesRegex(CalculationError, "divide by zero"):
            calculate("1 / (2 - 2)")

    def test_display_rounding_and_reuse(self):
        self.assertEqual(format_result(calculate("1/3")), "0.333333333333")
        self.assertEqual(format_result(calculate("2.5000")), "2.5")
        self.assertEqual(format_result(calculate("-0")), "0")
        for expression in ("1e20", "1e-20", "-1/3"):
            displayed = format_result(calculate(expression))
            self.assertEqual(format_result(calculate(f"({displayed})")), displayed)

    def test_expression_limit(self):
        with self.assertRaises(CalculationError):
            calculate("1" * 1001)


if __name__ == "__main__":
    unittest.main()
