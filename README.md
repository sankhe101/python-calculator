# Python Desktop Calculator

An offline Tkinter calculator built while learning Python and Git. Requires Python with Tkinter; no third-party packages are needed.

## Setup and launch (Windows PowerShell)

```powershell
cd "C:\Users\sankh\OneDrive\Documents\python-calculator"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python app.py
```

Create `.venv` only once. If activation is blocked, launch directly:

```powershell
.\.venv\Scripts\python.exe app.py
```

See [SETUP-GUIDE.md](SETUP-GUIDE.md) for environment details.

## Using the calculator

Type an expression or click the keypad, then press Enter or Calculate.
Supports `+`, `-`, `*` or `×`, `/` or `÷`, decimals, negative numbers, parentheses, and postfix `%`. Multiplication and division precede addition and subtraction. Scientific notation such as `1e-7` is supported so small or large displayed results can be reused.

Examples: `2 + 3 * 4 = 14`, `(2 + 3) * 4 = 20`, `0.1 + 0.2 = 0.3`.

Percent always means division by 100: `50% = 0.5`, `200 * 10% = 20`, and `200 + 10% = 200.1`.

- Backspace edits the input; Escape or Clear clears input.
- Reset clears input and resets the result to zero, keeping history.
- Successful calculations appear newest first in session history.
- Select an entry and choose Reuse selected result, or double-click it. The result is inserted at the cursor, replacing selected input.
- Clear history removes all history. Closing the app also discards history.
- Errors leave the app usable and do not create history entries.

## Tests

```powershell
.\.venv\Scripts\python.exe -m unittest -v
```

Tests cover the calculation engine and interface callbacks with real Tk widgets. Interface tests require a desktop environment with Tkinter.

Manual check: launch the app, calculate the examples above with both keyboard and buttons, try `1/0`, reuse a history result, clear history, and reopen the app to confirm history starts empty. Check readable labels, scrolling, and Tab navigation.

## Code and limitations

- `calculator.py`: tokenizer and arithmetic parser using Decimal; never evaluates Python code.
- `app.py`: Tkinter window, editing controls, and session history.
- `test_calculator.py` and `test_app.py`: automated tests.

Calculations use 50-digit decimal precision; display rounds to 12 significant digits. Reusing a result uses its displayed rounded value. Expressions are limited to 1000 characters. Powers, implicit multiplication (`2(3)`), scientific functions, saved history, and an installer are outside version one. Other operating systems have not been verified.

## Save your work with GitHub Desktop

Review Changes on `feature/calculation-engine`, commit with a descriptive message, and Push origin. Once reviewed, open a pull request to `main` and merge it. The Git learning milestones in the PRD still need to be completed; implementing the app does not automatically commit, push, merge, or tag it.
