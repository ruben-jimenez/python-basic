"""
Exercise from: https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
Code created by Ruben Jimenez
"""
import random


def run():
    print("PC Guess the number. Now the PC will guess the number")
    print("Think on a number, and help the PC to guess it.")
    print("Type < if is low > if is high or = if the number is correct. Another input will close the game.")
    num = random.randint(1, 100)
    lesshigh = [1,100]
    while True:
        print(f'The number is {num}?')
        userInput = input('User input: ')
        if userInput == '<':
            num = random.randint(lesshigh[0]+1,num)
        elif userInput == '>':
            num = random.randint(num,lesshigh[1]-1)
        elif userInput == '=':
            print('I win!')
            break
        else:
            break
        

if __name__ == "__main__":
    run()