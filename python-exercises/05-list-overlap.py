"""
Exercise from: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
Code created by Ruben Jimenez
"""

def run():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for element in a:
        if element in b and element not in c:
            c.append(element)
    print(c)


if __name__ == '__main__':
    run()