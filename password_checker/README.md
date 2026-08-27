# Password Checker

## Purpose
A simple command-line program that prompts a user to enter a password and then confirms it by asking them to re-enter it. The program verifies whether both entries match and loops until the user provides a matching password.

## Features
- Prompts the user to enter a password
- Re-prompts the user to confirm the password
- Loops indefinitely until the passwords match
- Prints a success message when the passwords match and exits gracefully
- Uses a colorful ASCII art banner on startup

## How to Run

```bash
python password_check.py
```

No external dependencies are required — the script uses only the Python standard library.

## Usage Example

```
Please enter a password: MySecret123
Please re-enter the password to check if it matches: MySecret123
Good job! The password 'MySecret123' matches.
Exiting the program. Goodbye!
```

## File
| File | Description |
|------|-------------|
| `password_check.py` | Main script |
