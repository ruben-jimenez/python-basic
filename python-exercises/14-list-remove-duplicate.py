"""
Exercise from: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
Code created by Ruben Jimenez
"""

def get_wfunct(a):
    b = []
    for element in a:
        if element not in b:
            b.append(element)
    return b

def get_wset(a):
    return list(set(a))

def run():
    a = [1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 6, 8, 9, 2]
    print(get_wset(a))
    print(get_wfunct(a))


if __name__ == "__main__":
    run()