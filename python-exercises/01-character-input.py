"""
Exercise from: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
Code created by Ruben Jimenez
"""

import datetime

def run():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    copies = int(input('Enter a number to copy the final mesage: '))
    now = datetime.datetime.now()
    yearstohundred = str((100 - age) + now.year)
    print(('Hello, your name is ' + name + ', and you will turn 100 years old on ' + yearstohundred + '\n') * copies)


if __name__ == '__main__':
    run()