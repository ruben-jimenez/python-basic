"""
Exercise from: https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
Code created by Ruben Jimenez
"""
# Python imports
import random

def generate_password(level):
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '*']

    characters = caps + lower + numbers + symbols
    password = []

    if level == 1:
        for i in range(8):
            random_char = random.choice(characters)
            password.append(random_char)
    else:
        for i in range(12):
            random_char = random.choice(characters)
            password.append(random_char)
    newpassword = ''.join(password)
    return newpassword


def run():
    print("Pick which password type you want.")
    passLevel = int(input("1: weak   2: strong: "))
    password = generate_password(passLevel)
    print("Your new password is",password)


if __name__ == "__main__":
    run()