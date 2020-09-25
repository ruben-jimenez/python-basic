"""
Exercise from: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
Code created by Ruben Jimenez
"""
def run():
    print('Rock Paper Scissors Game')
    while True:
        print("Choose * S:Scissors * R:Rock * P:Paper * Q:Quit *")
        pOne = input("Player 1: ")
        pTwo = input("Player 2: ")
        if pOne == pTwo:
            print('Draw, try again!')
        elif pOne == 'S' and pTwo == 'P' or pOne == 'P' and pTwo == 'R' or pOne == 'R' and pTwo == 'S':
            print('Player 1 Wins!')
        elif pTwo == 'S' and pOne == 'P' or pTwo == 'P' and pOne == 'R' or pTwo == 'R' and pOne == 'S':
            print('Player 2 Wins!')
        elif pOne == 'Q' or pTwo == 'Q':
            break
        else:
            print('Incorrect input. Try again!')


if __name__ == '__main__':
    run()