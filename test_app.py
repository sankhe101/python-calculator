"""Integration checks using real Tk widgets without showing a window."""
import tkinter as tk
import unittest
from app import CalculatorApp


class InterfaceTests(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = CalculatorApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_buttons_and_keyboard_use_same_calculation(self):
        for key in ("2", "+", "3", "×", "4"):
            self.app.buttons[key].invoke()
        self.app.evaluate()
        self.assertEqual(self.app.result.get(), "14")
        self.app.clear_input()
        self.app.expression.set("2+3*4")
        self.app.evaluate(tk.Event())
        self.assertEqual(self.app.result.get(), "14")
        self.assertTrue(self.app.entry.bind("<Return>"))
        self.assertTrue(self.root.bind("<Escape>"))

    def test_errors_do_not_add_history_and_app_recovers(self):
        for expression in ("1/0", "2+"):
            self.app.expression.set(expression)
            self.app.evaluate()
        self.assertEqual(self.app.history, [])
        self.app.expression.set("50%")
        self.app.evaluate()
        self.assertEqual(self.app.result.get(), "0.5")
        self.assertEqual(len(self.app.history), 1)

    def test_history_reuse_clear_and_reset(self):
        for expression in ("1+2", "-5+2"):
            self.app.expression.set(expression)
            self.app.evaluate()
        self.assertEqual(self.app.history[0], ("-5+2", "-3"))
        self.app.clear_input()
        self.app.history_list.selection_set(0)
        self.app.reuse_result()
        self.assertEqual(self.app.expression.get(), "(-3)")
        self.app.insert("+4")
        self.app.evaluate()
        self.assertEqual(self.app.result.get(), "1")
        self.app.clear_history()
        self.assertEqual(self.app.history_list.size(), 0)
        self.assertEqual(self.app.history, [])
        self.app.reset()
        self.assertEqual(self.app.result.get(), "0")
        self.assertEqual(self.app.expression.get(), "")

    def test_editing(self):
        self.app.insert("123")
        self.app.backspace()
        self.assertEqual(self.app.expression.get(), "12")
        self.app.entry.selection_range(0, tk.END)
        self.app.insert("9")
        self.assertEqual(self.app.expression.get(), "9")


if __name__ == "__main__":
    unittest.main()
