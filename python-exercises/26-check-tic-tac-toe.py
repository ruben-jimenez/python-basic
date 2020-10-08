"""
Exercise from: https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
Code created by Ruben Jimenez
"""
def get_winner(game):
    #rows
    for x in range(3):
        row = set([ game[x][0], game[x][1], game[x][2] ])
        if len(row) == 1 and game[x][0] != 0:
            return game[x][0]
    #cols
    for x in range(3):
        row = set([ game[0][x], game[1][x], game[2][x] ])
        if len(row) == 1 and game[0][x] != 0:
            return game[0][x]
    #diagonal
    diag1 = set([ game[0][0], game[1][1], game[2][2] ])
    diag2 = set([ game[2][0], game[1][1], game[0][2] ])

    if len(diag1) == 1 or len(diag2) == 1 and game[1][1] != 0:
        return game[1][1]

def run():
    win = 0
    game = [
        [2, 1, 0],
        [2, 1, 0],
        [2, 2, 1]
    ]
    winner = get_winner(game)
    if winner != 0:
        print(f'Player {winner} wins!')
    
if __name__ == "__main__":
    run()