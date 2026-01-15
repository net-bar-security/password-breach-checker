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

## Usage Instructions for Password Breach Checker

This guide will walk you through the steps to run the Password Breach Checker script. This tool allows you to check if your password has been compromised in known data breaches.

## Requirements

- **Python 3.x**
- **Internet connection** (required for HIBP API access)
- **requests >= 2.25.0** (already listed in `requirements.txt`)
- **Git** (optional, only required if cloning the repository)

---

## Step-by-Step Installation Guide

### Step 1: Install Python 3

#### Windows
1. Download Python from: https://www.python.org/downloads/
2. During installation, check **“Add Python to PATH”**
3. Verify installation:
   ```bash
   python --version
   ```
   
**Linux** (Debian / Ubuntu / Kali)
```bash
sudo apt update
sudo apt install python3 python3-pip -y
python3 --version
```

**macOS**
```bash
brew install python
python3 --version
```

### Step 2 (Optional): Install Git
Git is only required if you want to clone the repository.

**Windows**
Download Git from: https://git-scm.com/download/win
Verify:

```bash
git --version
```

**Linux**
```bash
sudo apt install git -y
```

**macOS**
```bash

brew install git
```

### Installation Methods
**Method A: Clone the Repository (Recommended)**
```bash

git clone https://github.com/net-bar-security/password-breach-checker.git
cd password-breach-checker
```

**Method B: Download Without Git**
1. Open: https://github.com/net-bar-security/password-breach-checker
2. Click Code → Download ZIP
3. Extract the ZIP file
4. Open a terminal in the extracted folder

#### Install Dependencies
The repository already includes a requirements.txt file.

```bash
pip install -r requirements.txt
```
If pip points to Python 2 on your system, use:

```bash
pip3 install -r requirements.txt
```

---

## Usage
Follow the instructions below based on your operating system. All commands should be run **from the project directory** (the folder containing `password_breach_checker.py`).

### Step 1: Open a Terminal

#### Linux (Kali, Ubuntu, Debian, etc.)
- Open **Terminal**
- Applications → Terminal  
- Or press `Ctrl + Alt + T`

#### macOS
- Open **Terminal**
- Spotlight Search (`Cmd + Space`) → type `Terminal`

#### Windows
- Open **Command Prompt** or **PowerShell**
- Press `Win + R` → type `cmd` or `powershell`
- If using **WSL**, open your Linux terminal instead

---

### Step 2: Navigate to the Project Directory

If you cloned the repository, navigate to it using `cd`:
```bash
cd password-breach-checker
```

Verify you are in the correct directory:
**Linux / macOS**
```bash
ls
```

**Windows**
```bash
dir
```

You should see:
- password_breach_checker.py
- requirements.txt
- README.md
- LICENSE


### Step 3: Run the Script

Use one of the following commands:
```bash
python3 password_breach_checker.py
```
or:
```bash
python password_breach_checker.py
```
Note: On Kali Linux and most Linux distributions, python3 is required.

### Step 4: Enter Your Password 

**Important Notice**
Your password will not be visible while typing:
- No characters
- No asterisks (`*`)
- No dots

This is **expected and secure behavior**.
The script uses Python’s `getpass` module to prevent shoulder-surfing and screen logging.

When prompted: `Enter your password to check for breaches:` type your password normally and press `Enter`.

### Step 5: Review the Result

The script will report one of the following:
- Password not found in known data breaches
- Password found, including how many times it appeared
- Network or API error (e.g., no internet connection)

Example output:

**`WARNING: Your password has been found in 3 known data breaches!`**
OR
**`Recommendation: Change your password immediately`**

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
