import random
def main():
    board = generateBoard()
    winner = False
    while winner == False:
        playerTurn(board)
        winner = checkForWin(board)
        if winner == True:
            break
        computerTurn(board)
        winner = checkForWin(board)
        if winner == True:
            break


def generateBoard():
    board = [['-','-','-','-','-','-','-'],
             ['-','-','-','-','-','-','-'],
             ['-','-','-','-','-','-','-'],
             ['-','-','-','-','-','-','-'],
             ['-','-','-','-','-','-','-'],
             ['-','-','-','-','-','-','-']]

    return board
    
def playerTurn(board):
    for item in board:
        print(item)
    validInput = False
    while validInput == False:
        userInput = eval(input("Enter a column 1-7: "))
        if userInput < 1 or userInput > 7:
            print("Choose a valid column")
        else:
            validInput = True
    userInput = userInput - 1
    for row in reversed(board):
        if row[userInput] != "-":
            continue
        else:
            row[userInput] = "O"
            break
    
def computerTurn(board):
    com = random.randint(0,6)
    for row in reversed(board):
        if row[com] != "-":
            continue
        else:
            row[com] = "X"
            break

def checkForWin(board):
    winner = checkHorizontal(board)
    if winner == True:
        return winner
    winner = checkVertical(board)
    if winner == True:
        return winner
    winner = checkDiagonal(board)
    if winner == True:
        return winner
    return False

def checkHorizontal(board):
    winner = False
    for row in board:
        user = 0
        com = 0
        for j in row:
            if j == "O":
                user += 1
            if j != "O":
                user = 0
            if j == "X":
                com += 1
            if j != "X":
                com = 0
            if user == 4:
                winner = True
                for item in board:
                    print(item)
                print("you win!")
                return winner
            if com == 4:
                for item in board:
                    print(item)
                winner = True
                print("computer win!")
                return winner
    return winner

def checkVertical(board):
    winner = False
    for i in range(7):
        user = 0
        com = 0
        for row in board:
            j = row[i]
            if j == "O":
                user += 1
            if j != "O":
                user = 0
            if j == "X":
                com += 1
            if j != "X":
                com = 0
            if user == 4:
                for item in board:
                    print(item)
                winner = True
                print("you win!")
                return winner
            if com == 4:
                winner = True
                for item in board:
                    print(item)
                print("computer win!")
                return winner
    return winner

def checkDiagonal(board):
    for x in range(6):
        for y in range(7):
            winner = get_diagonal_right(board, x, y)
            if winner == True:
                return winner
            winner = get_diagonal_left(board, x, y)
            if winner == True:
                return winner
    return winner

def get_diagonal_right(board,x,y):
    diagonal = []
    while x < 6 and y < 7:
        diagonal.append(board[x][y])
        x += 1
        y += 1
    winner = connected(board, diagonal, 4)
    return winner

def get_diagonal_left(board,x,y):
    diagonal = []
    while x < 6 and y < 7:
        diagonal.append(board[x][y])
        x += 1
        y -= 1
    winner = connected(board, diagonal, 4)
    return winner

def connected(board,lst,k):
    user = 0
    com = 0
    for i in lst:
        if i == "X":
            com += 1
        else:
            com = 0
        if i == "O":
            user += 1
        else:
            user = 0
        if user >= k:
            for item in board:
                print(item)
            print("Player Won!")
            return True
        if com >= k:
            for item in board:
                print(item)
            print("Computer Won!")
            return True
    else:    
        return False
    
if __name__ == "__main__":
    main()