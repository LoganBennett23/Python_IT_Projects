# Python IT Projects

A collection of Python programs focused on IT topics including password security and networking knowledge.

---

## Projects

### 🔐 [Password Checker](./password_checker/)
**File:** `password_checker/password_check.py`

A simple CLI program that prompts a user to enter a password and then confirms it by asking them to re-enter it. Loops until both entries match, then exits with a success message.

---

### 🔑 [Pass CG — Password Generator & Checker (CLI)](./pass_cg/)
**File:** `pass_cg/pass_CG.py`

A full-featured command-line password utility with a menu-driven interface. Supports:
- Generating a random password of any length
- Checking the strength of any password against common security criteria
- Generating a memorable passphrase from a word list (with optional digits/symbols)

---

### 🖥️ [Pass CG GUI — SecurePass Password Generator](./pass_cg_gui/)
**File:** `pass_cg_gui/Pass_CG_GUI.py`

A polished dark-themed desktop application (Tkinter) that brings all the features of Pass CG into a graphical interface. Uses Python's `secrets` module for cryptographically secure password generation. Includes a password strength evaluator with visual feedback.

---

### 🌐 [Networking Ports Quiz](./networking_ports_quiz/)
**File:** `networking_ports_quiz/networking_ports_quiz.py`

An interactive CLI quiz that tests knowledge of common networking protocol port numbers and their TCP/UDP types. Randomly selects a protocol each round and provides immediate feedback. Great for CompTIA Network+ or general IT certification study.

---

## Requirements

All projects use only the Python standard library, except **Pass CG GUI** which requires `tkinter` (included with most standard Python installations).

- Python 3.x
- No `pip install` needed
