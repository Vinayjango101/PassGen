import random
import string


def letter_numbers_punctuation():
    CHARS = string.ascii_letters + string.digits + string.punctuation
    pass_length = int(input("Enter max length of password: "))
    password = ''.join(random.choice(CHARS) for _ in range(pass_length))
    print("Generated password:", password)


def letter_only():
    CHARS = list(string.ascii_lowercase)  # or use string.ascii_letters for both cases
    password_length = int(input("Enter password length: "))
    password = ''.join(random.choice(CHARS) for _ in range(password_length))
    print("Generated password:", password)


banner = """
==============================
      PASSWORD GENERATOR
           v0.1
==============================
1. Letters, Numbers & Punctuation
2. Letters Only
"""

print(banner)

user_choice = input("Enter your choice (1 or 2): ")

if user_choice == "1":
    letter_numbers_punctuation()
elif user_choice == "2":
    letter_only()
else:
    print("Invalid choice. Please enter 1 or 2.")
