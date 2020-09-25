"""
Exercise from: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
Code created by Ruben Jimenez
"""
def run():
    check = input('Palindrome validator. Enter a string: ')
    if check == check[::-1]:
        print('The string ' + check + ' is a palindrome')
    else:
        print('The string ' + check + ' isn\'t a palindrome')



if __name__ == '__main__':
    run()