import main


player1 = main.Player("P1",'x')
player2 = main.Player("P2",'x')

board = main.Board(1)
board.createBoard()

def play(sym):
    board.print()
    p = int(input("Choose Postion:"))
    
    for i in range(3):
        for j in range(3):
            if board.board[i][j] == p:
                board.board[i][j] = sym

print("-------------------------------------------")
print("----------------TIC TAC TOE----------------")
print("-------------------------------------------\n\n")
print("Player01 is X")
print("Player02 is O\n")


while(not main.checkWin(board.board)):
    # Player 01
    play('X')
    if main.checkWin(board.board): break
    play('O')
    
    