# Pass CG — Password Generator & Checker (CLI)

## Purpose
A command-line password utility with three core features: generating a random password, checking the strength of any password, and generating a human-friendly "memorable" password from a word list. This was the original CLI version before the GUI was built.

## Features

### 1. Generate a Random Password
- User specifies the desired password length
- Password is built from letters (upper + lower), digits, and punctuation
- Displayed in bold green text

### 2. Check a Password
Evaluates a given password against five criteria and reports pass/fail for each:
- Minimum 8 characters
- Contains an uppercase letter
- Contains a lowercase letter
- Contains a digit
- Contains a special character

### 3. Generate a Memorable Password
- Choose between a built-in default word list or provide your own comma-separated word list
- Optionally append a random digit
- Optionally append a random special character
- Choose how many words to combine
- Option to save the generated password to `memorable_passwords.txt`

## How to Run

```bash
python pass_CG.py
```

No external dependencies required — uses only the Python standard library (`random`, `string`).

## Usage Example

```
Please select an option:
1. Generate a random password
2. Check a password
3. Generate a memorable random password with words
4. Exit
Enter your choice: 1
Enter the desired length of the password: 16
Generated password: aB3$xQ!9mR2#kLpZ
```

## Files
| File | Description |
|------|-------------|
| `pass_CG.py` | Main script |
| `memorable_passwords.txt` | Auto-created when passwords are saved (not tracked in git) |
