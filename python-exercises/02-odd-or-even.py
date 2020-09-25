"""
Exercise from: https://www.practicepython.org/solution/2014/02/15/02-odd-or-even-solutions.html
Code created by Ruben Jimenez
"""

def run():
    num = int(input('Enter a number to check: '))
    check = int(input('Enter a number to divide by: '))
    if num % 4 == 0:
        print(num, 'is a multiple of 4')
    if num % 2 == 0:
        print(num, 'is an even number')
    else:
        print(num, 'is an odd number')

    if num % check == 0:
        print(num, 'divides evenly by', check)
    else:
        print(num, 'does not divide evenly by', check)

if __name__ == '__main__':
    run()