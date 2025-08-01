import random
import string


def letter_numbers_punctuation():
    CHARS = string.ascii_letters + string.digits + string.punctuation

    pass_length = int(input("Enter max length of password: "))

    password = ''.join(random.choice(CHARS) for _ in range(pass_length))

    print("Generated password:", password)



def letter_only():
    CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v',
             'w', 'x', 'y', 'z']

    password_length = int(input("Enter password length: "))

    password = ''.join(random.choice(CHARS) for x in range(password_length))

    print("Generated Password - " + password)




banner = """

PASSWORD GENERATOR
v0.1

"""
print(banner)


user_choice = input("Enter your choice: ")
if user_choice == "1":
    letter_numbers_punctuation()
elif user_choice == "2":
    letter_only()
