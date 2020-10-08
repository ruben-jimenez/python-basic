"""
Exercise from: https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
Code created by Ruben Jimenez
"""
import random

def get_cows(number, userInput):
    cows = 0
    for element in userInput:
        if element in number:
            cows += 1
    return cows


def get_bulls(number, userInput):
    bulls = 0
    for x in range(4):
        if number[x] == userInput[x]:
            bulls += 1
    return bulls

def game(number):
    userInput = 0
    tries = 0
    while number != userInput:
        userInput = input("Enter a number: ")
        cows = get_cows(number, userInput)
        bulls = get_bulls(number, userInput)
        cows = cows - bulls
        tries += 1
        print(f'You have {cows} cows, {bulls} bulls. Try N {tries}')


if __name__ == "__main__":
    number = str(random.randrange(1000,9999))
    print(number)
    game(number)
    print(f"You win! Number is {number}")