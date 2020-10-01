"""
Exercise from: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
Code created by Ruben Jimenez
"""

def get_Fibonacci(a):
    return a[-2] + a[-1]

def run():
    limit = int(input("Enter a number of Fibonacci numbers you want to generate: "))
    a = [0, 1]
    while len(a) < limit:
        a.append(get_Fibonacci(a))
    print(a)


if __name__ == "__main__":
    run()