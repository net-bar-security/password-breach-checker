"""
Password Breach Checker

This tool checks whether a password has appeared in known data breaches
using the Have I Been Pwned (HIBP) Passwords API and the k-anonymity model.

SECURITY NOTICE:
- This script NEVER sends the full password over the network.
- Only the first 5 characters of a SHA-1 hash are transmitted.
- Designed for educational and defensive security purposes only.

This project demonstrates:
- Secure API consumption
- Privacy-preserving design
- Linux-based defensive security scripting

This tool is NOT intended for malicious use.

NOTE:
- Excessive automated requests may be rate-limited by the HIBP service.
- Use responsibly and avoid bulk password checking.
"""

import hashlib
import requests
import getpass


def check_password_breach(password):
    """
    Securely check if a password has been exposed in data breaches
    using the Have I Been Pwned k-anonymity model.

    API Reference:
    https://haveibeenpwned.com/API/v3#PwnedPasswords
    """

    # Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    # Split hash for k-anonymity
    hash_prefix = sha1_password[:5]
    hash_suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
    headers = {
        "User-Agent": "Password-Breach-Checker-Kali"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print("Error: Unable to check password breach status")
            return None

        for line in response.text.splitlines():
            suffix, count = line.split(":")
            if suffix == hash_suffix:
                return int(count)

        return 0

    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None


def main():
    print("Enter your password to check for breaches:")
    password = getpass.getpass()

    breach_count = check_password_breach(password)

    if breach_count is None:
        print("Unable to complete password breach check")
        input("Press Enter to exit...")  # Wait for user interaction
        exit(2)
    elif breach_count > 0:
        print(f"WARNING: Your password has been found in {breach_count} known data breaches!")
        print("Recommendation: Change your password immediately")
        input("Press Enter to exit...")  # Wait for user interaction
        exit(1)
    else:
        print("Good news! Your password has not been found in known data breaches.")
        input("Press Enter to exit...")  # Wait for user interaction
        exit(0)


if __name__ == "__main__":
    main()

# License:
# MIT License
# Copyright (c) 2026 Netzer Bar-On
# https://opensource.org/licenses/MIT
