class Board:

    def __init__(self,bNum):
        self.bNum = bNum

    def createBoard(self):
        self.bNum = [[1,2,3],[4,5,6],[7,8,9]]
    
    def print(self):
        for x in self.bNum : print(x)


class Player:

    def __init__(self,name,symbol,score=0):
        self.name = name
        self.symbol = symbol
        self.score = score
    
    def print(self):
        print(self.name)
        print(self.score)
        print(self.symbol)


def checkWin(board):
    # rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return 1
    
    # Coloms
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return 1
    
    # Diagnal
    if board[0][0] == board[1][1] == board[2][2]:
        return 1
    
    if board[0][2] == board[1][1] == board[2][0]:
        return 1
    

