# Password Strength Checker

import string

def check_password_strength(password):
    score = 0

    # Conditions that increase password strength
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    # Decide strength based on score
    if score <= 2:
        return "WEAK"
    elif score == 3:
        return "MEDIUM"
    else:
        return "STRONG"


# Program starts here
print("Enter a password to check its strength:")
user_password = input("> ")

strength = check_password_strength(user_password)

print("\nPassword Strength:", strength)
