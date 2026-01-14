# Password Breach Checker

A privacy-preserving Python tool that checks whether a password has appeared in known data breaches using the **Have I Been Pwned (HIBP)** Passwords API.  
Designed for **Kali Linux**, Linux environments, and defensive security learning.

---

## Overview

This script allows users to safely verify if a password has been exposed in public data breaches **without ever transmitting the full password**.  
It uses the HIBP **k-anonymity model**, ensuring strong privacy guarantees.

---

## Features

- Uses SHA-1 hashing with k-anonymity
- Never sends full passwords over the network
- Displays breach occurrence count when found
- Secure terminal input (no password echo)
- Linux and Kali-friendly
- Defensive and educational use

---

## How It Works

1. The password is hashed locally using SHA-1
2. Only the first 5 characters of the hash are sent to the HIBP API
3. The API returns matching hash suffixes
4. The full hash comparison is performed locally
5. The script reports whether the password was found in breaches

---

## Installation

### Requirements
- Python 3.x
- `requests` library

Install dependencies:

```bash
pip3 install -r requirements.txt
