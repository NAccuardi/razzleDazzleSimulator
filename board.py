import random

board =[]


def createboard():
    random.seed(1)
    # TODO: Make this a fair board. 120/6 =20
    boardnums = []
    for x in range(1, 121):  # verify this is making the correct number.
        boardnums.append(random.randint(1, 6))
    return boardnums


def printends():
    for x in range(12):
        print("-", end=" ")


def printbody(board):
    print()
    print("|",end = " ")
    for x in range(len(board)):
        if x % 10 == 0 and x != 0:
            print("|")
            print("|", end=" ")
            print(board[x], end=" ")
        else:
            print(board[x], end=" ")
    print("|")


def printboard(board):
    printends()
    printbody(board)
    printends()
    print()
