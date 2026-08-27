# Pass CG GUI — SecurePass Password Generator (GUI)

## Purpose
A graphical (Tkinter) version of the Password Generator program. It provides the same core password generation and evaluation features as the CLI version (`pass_CG.py`) but inside a polished dark-themed desktop application window, making it more user-friendly and accessible.

## Features

### Random Password Generator
- Choose password length
- Toggle inclusion of: uppercase letters, lowercase letters, digits, and symbols
- Uses Python's `secrets` module for cryptographically secure randomness
- Guarantees at least one character from each selected type
- Copy result to clipboard with one click

### Memorable Password Generator
- Combine multiple words from the built-in default word list or a custom word list
- Choose a word separator
- Optionally append a random digit and/or a random special character
- Uses `secrets` for secure word selection
- Copy result to clipboard

### Password Evaluator / Strength Checker
Scores a given password on five criteria:
- At least 12 characters
- At least 8 characters
- Contains an uppercase letter
- Contains a lowercase letter
- Contains a digit
- Contains a special character

Visual feedback is provided for each criterion (pass/fail).

## Requirements

- Python 3.x
- `tkinter` — included with most standard Python installations

No third-party packages are needed.

## How to Run

```bash
python Pass_CG_GUI.py
```

> **Note:** `tkinter` requires a display environment. It will not run in a headless terminal without a virtual display (e.g., Xvfb).

## Application Window
| Attribute | Value |
|-----------|-------|
| Title | SecurePass // Password Generator |
| Default size | 880 × 600 |
| Minimum size | 820 × 560 |
| Theme | Dark (custom hacker-inspired color palette) |

## Files
| File | Description |
|------|-------------|
| `Pass_CG_GUI.py` | Main application script |
