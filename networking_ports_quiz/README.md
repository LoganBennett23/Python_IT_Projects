# Networking Ports Quiz

## Purpose
An interactive command-line quiz designed to help IT students and professionals memorize common networking protocol port numbers and their transport-layer types (TCP or UDP). Each round randomly selects a protocol from a built-in dictionary and asks the user to identify its port number and protocol type.

## Features
- Covers 15 common networking protocols
- Random question selection each round so no two quiz sessions are the same
- Two-part questions per round:
  1. What is the port number for this protocol?
  2. Is it TCP or UDP?
- Immediate right/wrong feedback with the correct answer shown on failure
- Loop-based design — keep practicing until you type `exit`
- Colorful startup banner using ANSI escape codes

## Protocols Covered

| Protocol | Port | Type |
|----------|------|------|
| HTTP     | 80   | TCP  |
| HTTPS    | 443  | TCP  |
| FTP      | 21   | TCP  |
| SSH      | 22   | TCP  |
| Telnet   | 23   | TCP  |
| SMTP     | 25   | TCP  |
| DNS      | 53   | UDP  |
| POP3     | 110  | TCP  |
| IMAP     | 143  | TCP  |
| SNMP     | 161  | UDP  |
| LDAP     | 389  | TCP  |
| RDP      | 3389 | TCP  |
| TFTP     | 69   | UDP  |
| SFTP     | 22   | TCP  |
| NTP      | 123  | UDP  |

## How to Run

```bash
python networking_ports_quiz.py
```

No external dependencies required — uses only the Python standard library (`random`).

## Usage Example

```
Welcome to the Networking Ports Quiz!
Type '1' to start the quiz or 'exit' to quit: 1
What is the port number for DNS?: 53
Correct!
What is the protocol type for this port? (TCP/UDP): UDP
Correct!
Type '1' to start the quiz or 'exit' to quit: exit
Exiting the quiz. Goodbye!
```

## Files
| File | Description |
|------|-------------|
| `networking_ports_quiz.py` | Main script |
