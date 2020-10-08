"""
Exercise from: https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
Code created by Ruben Jimenez
"""

def run(number):
    a = [1, 2, 3, 4, 7 ,9 ,14, 33, 41, 78, 99, 120]
    valid = False
    if number in a:
        valid = True
    else:
        valid = False
    return valid


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(run(number))