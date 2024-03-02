import supprt


player1 = supprt.Player("P1",'x')
player2 = supprt.Player("P2",'x')

board = supprt.Board(1)
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


while(True):
    # Player 01
    play('X')
    if supprt.checkWin(board.board): 
        player1.score += 1
        print("Player 01 Won")
        break
    
    # Player 02
    play('O')
    if supprt.checkWin(board.board): 
        player2.score += 1
        print("Player 02 Won")
        break
    
