# Product Requirements Document: Python Desktop Calculator

**Status:** Draft
**Audience:** Personal and student use
**Project goal:** Build a useful Python calculator while practicing Git through small, reviewable changes.

## 1. Overview

Create a desktop calculator that supports basic arithmetic, percentages, and calculation history. The app should work offline and provide a simple interface with clickable buttons and keyboard input.

The project also serves as a learning exercise in Python, desktop interfaces, and Git.

## 2. Goals

- Perform everyday calculations accurately.
- Provide clear feedback for invalid input.
- Let users review and reuse earlier calculations.
- Practice Git commits, branches, merges, and pull requests as features are developed.

## 3. First-Version Scope

| Feature | Requirement |
|---|---|
| Arithmetic | Support addition, subtraction, multiplication, and division. |
| Expressions | Support decimals, negative numbers, and parentheses using standard operation precedence. |
| Percentages | Treat `%` as division by 100: `50% = 0.5` and `200 × 10% = 20`. |
| Input | Support calculator buttons and keyboard entry. |
| Editing | Provide backspace, clear input, and reset controls. |
| Results | Show readable results without unnecessary trailing zeros. |
| History | Display successful calculations from the current session, newest first. |
| Reuse | Allow users to insert a previous result into the current input. |
| Clear history | Allow users to remove all session history. |
| Errors | Explain invalid expressions and division by zero without closing the app. |

**Excluded from version one:** Scientific functions, graphing, accounts, cloud sync, saved history between sessions, and an installer.

## 4. User Stories

- As a student, I want to enter expressions so I can perform everyday calculations.
- As a user, I want to correct input without starting over.
- As a user, I want to review calculation history so I can check previous work.
- As a user, I want clear error messages so I can fix a calculation.
- As a learner, I want to develop each feature on a Git branch so I can understand how changes are tracked and merged.

## 5. Interface Requirements

The main window contains:

- An expression field and a clearly visible result.
- A keypad with digits, arithmetic operators, parentheses, decimal point, percentage, clear, backspace, and equals.
- A history panel with expressions and results.
- A clear-history control.

Keyboard controls:

| Key | Action |
|---|---|
| Digits and supported symbols | Enter an expression |
| Enter | Calculate |
| Backspace | Delete the last character |
| Escape | Clear the current input |

Use readable text, labeled controls, and a logical keyboard focus order. History should scroll without expanding the window indefinitely.

## 6. Technical Requirements

- **Language:** Python.
- **Desktop interface:** Tkinter.
- **Structure:** Keep calculation logic separate from interface code.
- **Expression handling:** Parse and validate supported expressions; do not evaluate arbitrary Python code.
- **Numeric behavior:** Use decimal arithmetic for ordinary calculations. Display recurring results with up to 12 significant digits.
- **Dependencies:** Prefer the Python standard library.
- **Testing:** Test calculation logic with Python’s `unittest`.
- **Documentation:** Include setup instructions, launch instructions, supported syntax, percentage behavior, and known limitations in the README.

The initial development target is Windows. Other operating systems may be supported later after verification.

## 7. Git Learning Plan

Each milestone produces a working, reviewable change.

| Milestone | Deliverable | Git practice |
|---|---|---|
| 1. Project setup | README, folder structure, and `.gitignore` | Initialize a repository, inspect changes, stage files, and make the first commit |
| 2. Calculation engine | Arithmetic, parsing, and meaningful tests | Create a feature branch, make focused commits, and inspect diffs |
| 3. Desktop interface | Window, keypad, and result display | Merge a completed feature branch into `main` |
| 4. Input and percentages | Keyboard controls, editing, and `%` behavior | Review changes and practice restoring an uncommitted edit |
| 5. History | Session history, result reuse, and clearing | Develop another feature branch and resolve a guided practice conflict |
| 6. Release | Verified app and completed documentation | Tag version `v1.0.0`; if using GitHub, open and merge a pull request |

Keep `main` runnable after each completed milestone. Commit messages should describe a concrete change, such as `Add division-by-zero handling`.

GitHub is optional; local Git practice is sufficient for the project.

## 8. Acceptance Criteria

Version one is complete when:

- `2 + 3 × 4` returns `14`.
- `(2 + 3) × 4` returns `20`.
- `-5 + 2` returns `-3`.
- `0.1 + 0.2` displays `0.3`.
- `50%` returns `0.5`.
- `200 × 10%` returns `20`.
- Division by zero displays a clear error and leaves the app usable.
- Invalid input displays an error without adding a successful history entry.
- Button input and keyboard input produce equivalent results.
- Successful calculations appear in history and their results can be reused.
- Clearing history removes all entries.
- Closing and reopening the app starts a fresh history.
- Calculation tests pass, and a manual interface check confirms the controls work.
- The README enables someone to launch the app.
- The Git history contains focused commits and merged feature branches.

## 9. Risks and Decisions

- **Percentage ambiguity:** Version one always interprets `%` as division by 100. For example, `200 + 10%` equals `200.1`.
- **Rounding:** Recurring decimals are rounded for display; this is an everyday calculator, not a financial calculation tool.
- **Learning scope:** Build one feature at a time and introduce Git concepts alongside the work.

## 10. Future Enhancements

Potential later additions include persistent history, scientific functions, themes, memory buttons, and packaged desktop releases.
