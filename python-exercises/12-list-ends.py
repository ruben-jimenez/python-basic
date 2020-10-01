"""
Exercise from: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
Code created by Ruben Jimenez
"""

def get_first_last_list(a):
    return [a[0], a[-1]]


def run():
    a = [5, 10, 15, 20, 25]
    print(get_first_last_list(a))


if __name__ == "__main__":
    run()