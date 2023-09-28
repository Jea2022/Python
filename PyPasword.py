"""
This Python code generates a random password based on user-specified
criteria for the number of letters, symbols, and numbers in the password.
"""

import random
# three list that contained letters, numbers and symbols are defined
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '%', '^', '&', '*', '(', ')', '-', '_', '+']

print("Welcome to the pyPassword Generator!")

# asking how many letters, numbers and symbols users wants in the poword
pw_letter = int(input("How many letters would like in your password?\n"))
pw_symbol = int(input("How many symbol would like in your password?\n"))
pw_number = int(input("How many number would like in your password?\n"))


password = []

# randomly selecting the letters based on the users input
for char in range(1, pw_number + 1):
    password.append(random.choice(letters))

# randomly selecting the symbols based on the users input
for sym in range(1, pw_symbol + 1):
    password += random.choice(symbols)

# randomly selecting the numbers based on the users input
for num in range(1, pw_number + 1):
    password += random.choice(numbers)

# shuffles the characters in the password list
random.shuffle(password)

# Changing list into string
password_str = ""
for char in password:
    password_str += char
print(f"Your password is: {password_str}")