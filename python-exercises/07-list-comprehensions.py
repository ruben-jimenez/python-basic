"""
Exercise from: https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
Code created by Ruben Jimenez
"""
def run():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even = [element for element in a if element % 2 == 0]
    print(even)


if __name__ == '__main__':
    run()