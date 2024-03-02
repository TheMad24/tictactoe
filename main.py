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


