# Password Breach Checker

## Overview

Password Breach Checker is a Python-based security utility that checks whether a password has appeared in known data breaches using the **Have I Been Pwned (HIBP)** Password API and the **k-anonymity** privacy model.

This project is intended for **educational and defensive cybersecurity purposes**, demonstrating secure API consumption, privacy-preserving design, and Linux-friendly scripting practices.

---

## Features

- Checks passwords against real-world breach data
- Implements HIBP’s **k-anonymity** model
- Never transmits full passwords
- No password storage or logging
- Simple command-line interface
- Suitable for Kali Linux and other Linux distributions

---

## How It Works

1. The password is hashed locally using **SHA-1**
2. Only the **first 5 characters** of the hash are sent to HIBP
3. The API returns matching hash suffixes
4. The script checks locally for a match
5. If found, the number of breach occurrences is reported

At no point is the plaintext password exposed or transmitted.

---

## Requirements

- Python 3.x
- pip install -r requirements.txt
- Internet connection (for HIBP API access)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/password-breach-checker.git
cd password-breach-checker
```
---

## Security & Privacy Notes

- Full passwords are **never transmitted**
- Uses the HIBP **k-anonymity** privacy model
- No password data is stored or logged
- No credentials are written to disk or retained beyond runtime
- Designed for responsible, defensive security use

HIBP API Reference:  
https://haveibeenpwned.com/API/v3#PwnedPasswords

---

## Ethical Use Statement

This tool is intended for **defensive security, education, and personal password hygiene** only.

Do **not** use this tool to test passwords that you do not own or do not have explicit authorization to assess.  
Misuse of this tool may violate privacy, ethical guidelines, or organizational policies.

---

## License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

## Author

### **Netzer Bar-On**
GitHub: https://github.com/net-bar-security
