"""
Exercise from: https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
Code created by Ruben Jimenez
"""

def printboard(size):
    lines = " --- "
    separator = "|   |"
    for x in range(size):
        if x == 0:
            print((lines*size) + "\n" + (separator*size) + "\n" + (lines*size))
        else:
            print((separator*size) + "\n" + (lines*size))


if __name__ == "__main__":
    size = int(input('What size do you want the game board? '))
    printboard(size)