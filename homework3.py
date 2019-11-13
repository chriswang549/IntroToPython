# Christopher Wang
# christwang
# 110969745
# CSE 101
# Homework #3

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!

# Part I
def find_starman(board):
    result = []
    for row in range (0, 5):
        for column in range (0, 5):
            if board[row][column] == '*':
                result.append(row+1)
                result.append(column+1)
            if (row == 4 and column == 4) and (board[4][4] != '*') and len(result) == 0:
                result.append(-1)
                result.append(-1)
    return result


# Part II
#                // board[row-1][column] == '*'
#                // board[row][column] == '.'
def move_up(board):
    result = []
    # FOR ALL THE ROWS IN THE RANGE 0 1 2 3 4 = 0-5
    #(row) = 1 2 3 4 5 [row] 0 1 2 3 4
    for row in range (0,5):
        for column in range (0,5):
            if board[row][column] == '*':
                while (len(result) == 0):
                    if row == 0:
                        result.append(-1)
                        result.append(-1)
                    elif board[row-1][column] == 'O':
                        board[row-1][column] = 'X'
                        board[row][column] = '.'
                        result.append(row)
                        result.append(column+1)
                    elif board[row-1][column] != '.' and board[row-1][column] !='F':
                        result.append(-1)
                        result.append(-1)
                    else:
                        board[row - 1][column] = '*'
                        board[row][column] = '.'
                        result.append(row)
                        result.append(column+1)
    return result


# Part III
def move_down(board):
    # 1195438101868657375/student_submission.py", line 64, in move_down
    # elif board[row + 1][column] == 'O' and len(result) == 0:
    # IndexError: list index out of range
    result = []
    for row in range (0, 5):
        for column in range (0, 5):
            if board[row][column] == '*':
                while (len(result) == 0):
                    if row == 4: # moves out of board
                        result.append(-1)
                        result.append(-1)
                    elif board[row + 1][column] == 'O':
                        board[row + 1][column] = 'X'
                        board[row][column] = '.'
                        result.append(row + 2)
                        result.append(column + 1)
                    elif board[row+1][column] == 'W': # wall
                        result.append(-1)
                        result.append(-1)
                    else:# 'F' or '.'
                        board[row + 1][column] = '*'
                        board[row][column] = '.'
                        result.append(row+2)
                        result.append(column+1)
    return result

# Part IV
def move_left(board):
    result=[]
    for row in range (0,5):
        for column in range (0,5):
            if board[row][column] == '*':
                while (len(result) == 0):
                    if column == 0:
                        result.append(-1)
                        result.append(-1)
                    elif board[row][column-1] == 'O':
                        board[row][column-1] = 'X'
                        board[row][column] = '.'
                        result.append(row+1)
                        result.append(column)
                    elif board[row][column-1] != '.' and board[row][column-1] !='F':
                        result.append(-1)
                        result.append(-1)
                    else:
                        board[row ][column-1] = '*'
                        board[row][column] = '.'
                        result.append(row+1)
                        result.append(column)
    return result


# Part V
def move_right(board):
    result = []
    for row in range(0, 5):
        for column in range(0, 5):
            if board[row][column] == '*':
                while (len(result) == 0):
                    if column == 4:
                        result.append(-1)
                        result.append(-1)
                    elif board[row][column + 1] == 'O':
                        board[row][column + 1] = 'X'
                        board[row][column] = '.'
                        result.append(row + 1)
                        result.append(column + 2)
                    elif board[row][column + 1] != '.' and board[row][column + 1] != 'F':
                        result.append(-1)
                        result.append(-1)
                    else:
                        board[row][column + 1] = '*'
                        board[row][column] = '.'
                        result.append(row + 1)
                        result.append(column + 2)
    return result


# Part VI
def move(board, movement):
    # recursion, when you call another function from a function and it returns back to original function
    result=[]
    if movement == 'U':
        result = move_up(board) # result = the returned value from the function move_up
    if movement == 'D':
        result = move_down(board)
    if movement == 'R':
        result = move_right(board)
    if movement == 'L':
        result = move_left(board)
    return result













def print_board(board):
    print("The updated game board:")
    row_num = 1
    print("   1  2  3  4  5")
    print("  ----------------")
    for row in board:
        print(str(row_num) + '| ' + '  '.join(row) + ' |')
        row_num += 1
    print("  ----------------" + "\n")


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your homework3.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Testing Part I
    board1 = [['*', '.', '.', '.', '.'],
              ['.', 'W', '.', '.', 'F'],
              ['.', '.', '.', 'W', '.'],
              ['.', '.', '.', 'W', '.'],
              ['F', '.', 'O', '.', '.']]

    board2 = [['.', 'W', 'W', 'W', 'W'],
              ['F', 'W', '.', '.', 'F'],
              ['.', 'O', '.', 'W', '.'],
              ['.', '.', '*', 'W', '.'],
              ['O', '.', 'O', '.', '.']]

    board3 = [['O', '.', '.', '.', '.'],
              ['.', '*', '.', '.', 'F'],
              ['.', '.', '.', 'O', '.'],
              ['.', '.', '.', 'O', '.'],
              ['F', '.', '.', '.', '.']]
    print("##### Part I ##### ")
    print("Testing find_starman() with board = board1: " + str(find_starman(board1)))
    print("Testing find_starman() with board = board2: " + str(find_starman(board2)))
    print("Testing find_starman() with board = board3: " + str(find_starman(board3)))
    print()

    # Testing Part II
    board1 = [['.', '.', '.', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['.', 'F', '*', 'F', '.'],
              ['.', '.', 'O', '.', 'W'],
              ['.', '.', 'O', '.', '.']]

    board2 = [['.', '*', '.', 'F', '.'],
              ['.', '.', 'W', 'F', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', 'W', '.', 'O', '.'],
              ['.', '.', '.', '.', '.']]

    board3 = [['.', 'O', '.', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', '.', 'F', '.', '.'],
              ['*', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part II ##### ")
    print("Testing move_up() with board = board1: " + str(move_up(board1)))
    print_board(board1)
    print("Testing move_up() with board = board2: " + str(move_up(board2)))
    print_board(board2)
    print("Testing move_up() with board = board3: " + str(move_up(board3)))
    print_board(board3)

    # Testing Part III
    board1 = [['.', '.', '.', '.', 'W'],
              ['.', '*', '.', '.', '.'],
              ['.', 'F', 'O', 'F', '.'],
              ['.', '.', 'O', '.', 'W'],
              ['.', '.', 'O', '.', '.']]

    board2 = [['.', '.', '.', 'F', '.'],
              ['.', '.', 'W', 'F', '.'],
              ['.', '*', 'F', '.', '.'],
              ['W', 'W', '.', 'O', '.'],
              ['.', '.', '.', '.', '.']]

    board3 = [['.', 'O', '.', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', '*', 'F', '.', '.'],
              ['W', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part III ##### ")
    print("Testing move_down() with board = board1: " + str(move_down(board1)))
    print_board(board1)
    print("Testing move_down() with board = board2: " + str(move_down(board2)))
    print_board(board2)
    print("Testing move_down() with board = board3: " + str(move_down(board3)))
    print_board(board3)

    # Testing Part IV
    board1 = [['.', '.', '.', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['.', 'F', 'O', 'F', '.'],
              ['.', '.', 'O', '.', 'W'],
              ['*', '.', 'O', '.', '.']]

    board2 = [['.', 'F', '.', 'F', '.'],
              ['.', '.', 'O', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', 'W', '.', 'O', '*'],
              ['.', '.', '.', '.', '.']]

    board3 = [['.', 'O', '.', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', '*', 'F', '.', '.'],
              ['W', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part IV ##### ")
    print("Testing move_left() with board = board1: " + str(move_left(board1)))
    print_board(board1)
    print("Testing move_left() with board = board2: " + str(move_left(board2)))
    print_board(board2)
    print("Testing move_left() with board = board3: " + str(move_left(board3)))
    print_board(board3)

    # Testing Part V
    board1 = [['F', 'F', 'F', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['.', 'F', 'O', 'F', '.'],
              ['.', '*', '.', '.', '.'],
              ['.', 'O', 'O', '.', '.']]

    board2 = [['F', 'W', 'F', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['.', '*', 'O', 'F', '.'],
              ['W', '.', '.', '.', '.'],
              ['.', 'W', 'O', '.', '.']]

    board3 = [['.', 'O', '.', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', '*', 'F', '.', '.'],
              ['W', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part V ##### ")
    print("Testing move_right() with board = board1: " + str(move_right(board1)))
    print_board(board1)
    print("Testing move_right() with board = board2: " + str(move_right(board2)))
    print_board(board2)
    print("Testing move_right() with board = board3: " + str(move_right(board3)))
    print_board(board3)

    # Testing Part VI
    board1 = [['.', 'W', 'W', '.', 'W'],
              ['F', 'F', '.', '.', 'F'],
              ['.', 'O', '.', 'W', '*'],
              ['.', '.', '.', 'W', '.'],
              ['O', '.', 'O', '.', '.']]

    board2 = [['.', 'F', '.', 'F', '.'],
              ['.', '.', 'O', '.', '.'],
              ['.', '.', 'O', '*', '.'],
              ['W', 'W', '.', 'O', '.'],
              ['.', '.', '.', 'W', '.']]

    board3 = [['F', 'W', 'F', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['W', '*', 'O', 'F', '.'],
              ['W', '.', '.', '.', '.'],
              ['.', 'W', 'O', '.', '.']]

    board4 = [['.', 'O', '.', '.', '.'],
              ['.', 'F', 'F', '.', '.'],
              ['W', '*', 'F', 'F', '.'],
              ['F', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part VI ##### ")
    print("Testing move() with board = board1, movement = 'U': " + str(move(board1, 'U')))
    print_board(board1)
    print("Testing move() with board = board2, movement = 'D': " + str(move(board2, 'D')))
    print_board(board2)
    print("Testing move() with board = board3, movement = 'L': " + str(move(board3, 'L')))
    print_board(board3)
    print("Testing move() with board = board4, movement = 'R': " + str(move(board4, 'R')))
    print_board(board4)