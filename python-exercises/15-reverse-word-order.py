"""
Exercise from: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
Code created by Ruben Jimenez
"""

def run():
    sentence = input('Write something long... ')
    result = sentence.split()
    print(" ".join(result[::-1]))


if __name__ == "__main__":
    run()