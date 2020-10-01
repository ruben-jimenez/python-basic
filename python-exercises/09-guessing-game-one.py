"""
Exercise from: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
Code created by Ruben Jimenez
"""

#imports
import random


def run():
    num = random.randint(1, 9)
    trackNum = 0
    while True:
        print('Try: ', trackNum)
        userIn = input('Guess the number: ')
        if userIn == 'exit':
            break
        elif int(userIn) < num:
            print('Try again. You guess too low')
            trackNum += 1
        elif int(userIn) > num:
            print('Try again. You guess too high')
            trackNum += 1
        else:
            print('You win! The number was ', num)
            break


if __name__ == '__main__':
    run()