"""
Exercise from: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
Code created by Ruben Jimenez
"""
#Python imports
import random


def run():
    ran1 = random.randint(7,13)
    ran2 = random.randint(5,10)

    a = random.sample(range(25), ran1)
    b = random.sample(range(25), ran2)

    list_overlap = [element for element in set(a) if element in b]
    print(list_overlap)


if __name__ == '__main__':
    run()