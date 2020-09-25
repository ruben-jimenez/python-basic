"""
Exercise from: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
Code created by Ruben Jimenez
"""

def run():
    num = int(input('Enter a number: '))
    x = range(1, num + 1)
    for elem in x:
        if num % elem == 0:
            print(elem)

if __name__ == '__main__':
    run()