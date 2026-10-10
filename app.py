"""Launch the desktop calculator with python app.py."""
import tkinter as tk
from tkinter import ttk
from calculator import CalculationError, calculate, format_result


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Python Calculator")
        root.geometry("720x540")
        root.minsize(640, 500)
        self.history = []
        self.expression = tk.StringVar()
        self.result = tk.StringVar(value="0")
        self.message = tk.StringVar(value="Enter an expression and press Enter or Calculate.")
        frame = ttk.Frame(root, padding=18)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(0, weight=3)
        frame.columnconfigure(1, weight=2)
        frame.rowconfigure(0, weight=1)
        left = ttk.Frame(frame)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 18))
        ttk.Label(left, text="Expression").pack(anchor="w")
        self.entry = ttk.Entry(left, textvariable=self.expression, font=("Segoe UI", 18))
        self.entry.pack(fill="x", pady=(5, 12))
        ttk.Label(left, textvariable=self.result, font=("Segoe UI", 24), wraplength=340).pack(anchor="e")
        ttk.Label(left, textvariable=self.message, wraplength=340).pack(fill="x", pady=12)
        keypad = ttk.Frame(left)
        keypad.pack(fill="both", expand=True)
        rows = [("Clear", "Backspace", "(", ")"), ("7", "8", "9", "÷"),
                ("4", "5", "6", "×"), ("1", "2", "3", "−"), ("0", ".", "%", "+")]
        self.buttons = {}
        for row_index, row in enumerate(rows):
            keypad.rowconfigure(row_index, weight=1)
            for column, label in enumerate(row):
                keypad.columnconfigure(column, weight=1)
                command = (self.clear_input if label == "Clear" else self.backspace
                           if label == "Backspace" else lambda text=label: self.insert(text))
                button = ttk.Button(keypad, text=label, command=command)
                button.grid(row=row_index, column=column, sticky="nsew", padx=2, pady=3)
                self.buttons[label] = button
        ttk.Button(left, text="= Calculate", command=self.evaluate).pack(fill="x", pady=(8, 4))
        ttk.Button(left, text="Reset input and result", command=self.reset).pack(fill="x")
        right = ttk.Frame(frame)
        right.grid(row=0, column=1, sticky="nsew")
        ttk.Label(right, text="Session history", font=("Segoe UI", 14)).pack(anchor="w")
        ttk.Label(right, text="Select a calculation to reuse its result.", wraplength=240).pack(anchor="w", pady=8)
        history_frame = ttk.Frame(right)
        history_frame.pack(fill="both", expand=True)
        self.history_list = tk.Listbox(history_frame, exportselection=False, font=("Segoe UI", 11))
        scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_list.yview)
        self.history_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.history_list.pack(side="left", fill="both", expand=True)
        self.history_list.bind("<Double-Button-1>", self.reuse_result)
        self.history_list.bind("<Return>", self.reuse_result)
        ttk.Button(right, text="Reuse selected result", command=self.reuse_result).pack(fill="x", pady=(8, 4))
        ttk.Button(right, text="Clear history", command=self.clear_history).pack(fill="x")
        self.entry.bind("<Return>", self.evaluate)
        self.entry.bind("<KP_Enter>", self.evaluate)
        root.bind("<Escape>", self.clear_input)
        self.entry.focus_set()

    def insert(self, text):
        if self.entry.selection_present():
            self.entry.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.entry.insert(tk.INSERT, text)
        self.entry.focus_set()

    def backspace(self):
        if self.entry.selection_present():
            self.entry.delete(tk.SEL_FIRST, tk.SEL_LAST)
        else:
            position = self.entry.index(tk.INSERT)
            if position:
                self.entry.delete(position - 1, position)
        self.entry.focus_set()

    def clear_input(self, event=None):
        self.expression.set("")
        self.message.set("Enter an expression and press Enter or Calculate.")
        self.entry.focus_set()
        return "break"

    def reset(self):
        self.clear_input()
        self.result.set("0")

    def evaluate(self, event=None):
        expression = self.expression.get()
        try:
            result = format_result(calculate(expression))
        except CalculationError as error:
            self.message.set(str(error))
            self.entry.focus_set()
            return "break"
        self.result.set(result)
        self.message.set("Calculated. History lasts until the app closes.")
        self.history.insert(0, (expression, result))
        self.history_list.insert(0, f"{expression} = {result}")
        self.entry.focus_set()
        return "break"

    def reuse_result(self, event=None):
        selection = self.history_list.curselection()
        if selection:
            self.insert(f"({self.history[selection[0]][1]})")
        else:
            self.message.set("Select a history entry first.")
        return "break"

    def clear_history(self):
        self.history.clear()
        self.history_list.delete(0, tk.END)
        self.message.set("History cleared.")


def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
