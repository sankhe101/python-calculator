# Calculator setup and learning guide

This guide records the setup steps for this project. We will expand it as we build the calculator and learn Git and GitHub.

## 1. Understand the Python environment

The base Python installation lives outside the project and provides the Python interpreter. A virtual environment gives this project its own Python environment and installed packages.

Our virtual environment will live here:

```text
C:\Users\sankh\OneDrive\Documents\python-calculator\.venv
```

Creating this guide does not install Python or create the environment. The previous automatic Python installation attempt was declined.

The calculator will use Python's standard library: Tkinter for the desktop interface, decimal arithmetic for calculations, and unittest for tests. No extra packages are currently required.

## 2. Open the project in PowerShell

```powershell
cd "C:\Users\sankh\OneDrive\Documents\python-calculator"
```

Run the following commands from this folder unless a step says otherwise.

## 3. Check base Python

```powershell
python --version
```

You should see a Python version. If the command fails or opens the Microsoft Store, install Python using the official [Windows setup instructions](https://docs.python.org/3/using/windows.html), then close and reopen PowerShell.

## 4. Create the virtual environment once

```powershell
python -m venv .venv
```

`-m venv` runs Python's environment creation tool. `.venv` is the folder it creates. You do not need to recreate it every time you work on the project.

## 5. Activate it when starting a new terminal

```powershell
.\.venv\Scripts\Activate.ps1
```

Your terminal prompt should begin with `(.venv)`. Activation makes the `python` command in this terminal use the project's environment. It does not affect other terminals.

Check the interpreter location:

```powershell
python -c "import sys; print(sys.executable)"
```

The output should end with:

```text
python-calculator\.venv\Scripts\python.exe
```

### If PowerShell blocks the activation script

You can use the environment directly without changing PowerShell settings:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m tkinter
```

For future Python commands, replace `python` with `.\.venv\Scripts\python.exe` when using this approach.

## 6. Check Tkinter

With the environment activated, run:

```powershell
python -m tkinter
```

A small demonstration window should open. Close it after checking. This confirms that the desktop interface library works.

## 7. Install packages only if needed later

With the environment activated, the general command is:

```powershell
python -m pip install PACKAGE_NAME
```

Replace `PACKAGE_NAME` with the actual package name. This is an example, not a command you need to run now. Using `python -m pip` installs into the environment used by that Python interpreter.

## 8. Leave the environment

```powershell
deactivate
```

This removes `(.venv)` from the prompt. It does not delete the environment. Closing the terminal also ends activation for that terminal.

## 9. Keep the environment out of GitHub

Before staging project files, create or update `.gitignore` with:

```gitignore
.venv/
__pycache__/
*.pyc
```

Git should track our source code, tests, and documentation. The virtual environment is generated locally and can be recreated.

## Everyday startup checklist

```powershell
cd "C:\Users\sankh\OneDrive\Documents\python-calculator"
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
```

## Run our first calculation example

The full desktop app is now available. Launch it with `python app.py` while the environment is activated, or `.\.venv\Scripts\python.exe app.py` without activation. See README.md for features and controls.

With the environment activated:

```powershell
python calculator.py
```

Expected output: `0.3`. This is currently a small addition example; the expression parser and desktop window will be added in later steps.

## Run automated tests

```powershell
python -m unittest -v
```

The tests check exact decimal addition and addition with a negative number. An `OK` result means all tests passed.

Without activation, use `.\.venv\Scripts\python.exe` in place of `python` in these commands.
