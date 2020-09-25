"""
Exercise from: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
Code created by Ruben Jimenez
"""

def run():
    num = int(input('Enter a number and the program will return a list with numbers less than this: '))
    a = [1,1,2,3,5,8,13,21,34,55,89]
    b = []
    c = []
    for element in a:
        if element <= 10:
            b.append(element)
    for element in a:
        if element <= num:
            c.append(element)
    print(b,'list with numbers less than 10')
    print(c,'list with numbers less than',num)

if __name__ == '__main__':
    run()