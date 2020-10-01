"""
Exercise from: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
Code created by Ruben Jimenez
"""

def get_number():
    return int(input('Give me a number: '))


def is_prime(number):
    if number > 0:
        for x in range (2, number -1 ):      #we can exclude 1 and number, both are visible by
            if number % x != 0:              #if number isn't evenly divisible by x, go to the next one
                continue
            elif number % x == 0:            #if number is evenly divisible by x, it can't be prime
                return False
        return True                          #number wasn't evenly divisible by any x, so it's prime
    elif number == 0:                        #0 is not prime
        return False
    else:                                    #Negative numbers are not prime
        return False


def run():
    print('Prime number validator')
    num = get_number()
    validation = is_prime(num)
    if validation == True:
        print('The number is prime!')
    else:
        print('The number is not prime!')


if __name__ == '__main__':
    run()