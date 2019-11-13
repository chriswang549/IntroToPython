# Christopher Wang
# christwang
# 110969745
# CSE 101
# Course Project

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!

from battleship import *

EMPTY = u"\u25A1"  # A white square
FOG = u"\u25A0"  # A black square
EXPLORED = u"\u2612"  # A square with an X inside
BOMB = u"\u25CE"  # Two concentric circles
SHIP = u"\u26F5"  # An icon of a sailboat
PLAYER_LOST = 100
COMPUTER_LOST = 200

# Part I
def is_valid_location(board, row, col):

   if row <= board.num_rows and col <= board.num_cols and row >= 0 and col >=0:
       return True
   else:
       return False

# Part II
def place_ship(board, row, col):

    if row < 1 or row > board.num_rows:
        return False
    if col < 1 or col > board.num_cols:
        return False
    for i in range(board.num_rows):
        if i == row - 1:
            for j in range(board.num_cols):
                if j == col - 1:
                    if board.cells[i][j] == EMPTY:
                        board.cells[i][j] = SHIP
                        return True

                    elif board.cells[i][j] == SHIP:
                        return False


# Part III
def attack(defender_board, row, col):
   if row < 1 or row > defender_board.num_rows:
       return False
   if col < 1 or col > defender_board.num_cols:
       return False
   for i in range(defender_board.num_rows):
       if i == row - 1:
           for j in range(defender_board.num_cols):
               if j == col - 1:
                   if defender_board.cells[i][j] == SHIP:
                       defender_board.cells[i][j] = BOMB
                       return True
                   if defender_board.cells[i][j] == EMPTY or FOG or EXPLORED:
                       defender_board.cells[i][j] = EXPLORED
                       return True
                   else:
                       return False






# Part IV
def game_status(player_board, ai_board):
   x = 0
   for i in range(player_board.num_rows):
       for j in range(player_board.num_cols):
           if player_board.cells[i][j] == SHIP:
               x = x + 1
   y = 0
   for i in range(ai_board.num_rows):
       for j in range(ai_board.num_cols):
           if ai_board.cells[i][j] == SHIP:
               y = y + 1
   if x<=0:
       return PLAYER_LOST
   if y<=0:
       return COMPUTER_LOST
   return 0





# Part V
def move_ship(board, current_location, new_location):
    x = current_location[0]
    y = current_location[1]
    a = new_location[0]
    b = new_location[1]


    if x < 1 or x > board.num_rows:
        return False
    if y < 1 or y > board.num_cols:
        return False
    if a < 1 or a > board.num_rows:
        return False
    if b < 1 or b > board.num_cols:
        return False
    if board.cells[a-1][b-1] != EMPTY and board.cells[a-1][b-1] != EXPLORED:
        return False
    if board.cells[x-1][y-1] != SHIP:
        return False

    board.cells[x-1][y-1] = EMPTY
    board.cells[a-1][b-1] = SHIP
    board.move_ability = False
    return True






# Part VI
def air_strike(attacker_board, defender_board, col):
#The function replaces all EMPTY cells in the given col of the defender board.cells with EXPLORED,
#replaces any SHIPs in the column with BOMBs, and leaves any other cells untouched.
    for i in range(defender_board.num_rows):
        for j in range (defender_board.num_cols):
            if j == col - 1:
                if defender_board.cells[i][j] == EMPTY:
                    defender_board.cells[i][j] = EXPLORED
                if defender_board.cells[i][j] == SHIP:
                    defender_board.cells[i][j] = BOMB
    if col < 1 or col > defender_board.num_cols:
        return False

    attacker_board.air_strike_ability = False
    return True




# Main program
if __name__ == '__main__':
    print("PART 1: ")
    part1_board = Board(4, 6)
    row = 2
    col = 3
    print("Testing is_valid_location() with board = 4X6, row = " + str(row) + ", col = " + str(col) + " " + str(
        is_valid_location(part1_board, row, col)))
    part1_board = Board(6, 7)
    row = -3
    col = 3
    print("Testing is_valid_location() with board = 6X7, row = " + str(row) + ", col = " + str(col) + " " + str(
        is_valid_location(part1_board, row, col)))
    part1_board = Board(5, 5)
    row = 6
    col = 6
    print("Testing is_valid_location() with board = 5X5, row = " + str(row) + ", col = " + str(col) + " " + str(
        is_valid_location(part1_board, row, col)))
    print()
    print("PART 2: ")
    part2_board = Board(4, 6)
    part2_board.cells[2][2] = SHIP
    part2_board.cells[3][3] = SHIP
    row = 3
    col = 2
    print("Testing place_ship() with board = 4X6, row = " + str(row) + ", col = " + str(col) + " " + str(
        place_ship(part2_board, row, col)))
    print(str(part2_board))
    part2_board = Board(6, 7)
    part2_board.cells[3][3] = SHIP
    part2_board.cells[4][4] = SHIP
    row = 7
    col = 6
    print("Testing place_ship() with board = 6X7, row = " + str(row) + ", col = " + str(col) + " " + str(
        place_ship(part2_board, row, col)))
    print(str(part2_board))
    part2_board = Board(5, 5)
    part2_board.cells[2][2] = SHIP
    part2_board.cells[3][3] = SHIP
    part2_board.cells[4][4] = SHIP
    row = 3
    col = 3
    print("Testing place_ship() with board = 5X5, row = " + str(row) + ", col = " + str(col) + " " + str(
        place_ship(part2_board, row, col)))
    print(str(part2_board))
    print()
    print("PART 3: ")
    part3_board = Board(4, 6)
    part3_board.cells[2][2] = SHIP
    part3_board.cells[3][3] = SHIP
    part3_board.cells[0][0] = SHIP
    row = 3
    col = 2
    print("Testing attack() with board = 4X6, row = " + str(row) + ", col = " + str(col) + " " + str(
        attack(part3_board, row, col)))
    print("Board:\n" + str(part3_board))
    part3_board = Board(6, 7)
    part3_board.cells[2][2] = SHIP
    part3_board.cells[3][3] = SHIP
    part3_board.cells[4][4] = SHIP
    row = 7
    col = 6
    print("Testing attack() with board = 6X7, row = " + str(row) + ", col = " + str(col) + " " + str(
        attack(part3_board, row, col)))
    print("Board:\n" + str(part3_board))
    part3_board = Board(5, 5)
    part3_board.cells[2][2] = SHIP
    part3_board.cells[3][3] = SHIP
    part3_board.cells[4][4] = SHIP
    row = 3
    col = 3
    print("Testing attack() with board = 5X5, row = " + str(row) + ", col = " + str(col) + " " + str(
        attack(part3_board, row, col)))
    print("Board:\n" + str(part3_board))
    print()
    print("PART 4: ")
    part4_board_player = Board(4, 6)
    part4_board_player.cells[2][2] = BOMB
    part4_board_player.cells[3][3] = BOMB
    part4_board_player.cells[0][0] = BOMB
    part4_board_ai = Board(4, 6)
    part4_board_ai.cells[2][2] = SHIP
    part4_board_ai.cells[3][3] = BOMB
    part4_board_ai.cells[0][0] = SHIP
    print("Testing game_status() with\nPlayer Board:\n" + str(part4_board_player) + "\n AI Board:\n" + str(
        part4_board_ai) + "\nYour Solution: " + str(game_status(part4_board_player, part4_board_ai)))
    print()
    part4_board_player = Board(6, 7)
    part4_board_player.cells[2][2] = BOMB
    part4_board_player.cells[3][3] = SHIP
    part4_board_player.cells[0][0] = BOMB
    part4_board_ai = Board(4, 6)
    part4_board_ai.cells[2][2] = BOMB
    part4_board_ai.cells[3][3] = BOMB
    part4_board_ai.cells[0][0] = BOMB
    print("Testing game_status() with\nPlayer Board:\n" + str(part4_board_player) + "\n AI Board:\n" + str(
        part4_board_ai) + "\nYour Solution: " + str(game_status(part4_board_player, part4_board_ai)))
    print()
    part4_board_player = Board(5, 5)
    part4_board_player.cells[2][2] = BOMB
    part4_board_player.cells[3][3] = SHIP
    part4_board_player.cells[0][0] = BOMB
    part4_board_ai = Board(4, 6)
    part4_board_ai.cells[2][2] = SHIP
    part4_board_ai.cells[3][3] = BOMB
    part4_board_ai.cells[0][0] = BOMB
    print("Testing game_status() with\nPlayer Board:\n" + str(part4_board_player) + "\n AI Board:\n" + str(
        part4_board_ai) + "\nYour Solution: " + str(game_status(part4_board_player, part4_board_ai)))
    print()
    print("PART 5: ")
    part5_board = Board(4, 6)
    part5_board.cells[2][2] = SHIP
    part5_board.cells[3][3] = BOMB
    part5_board.cells[0][0] = SHIP
    cur_loc = (3, 3)
    new_loc = (4, 6)
    print("Testing move_ship() with\nPlayer Board:\n" + str(part5_board) + "\nCurrent Location = " + str(
        cur_loc) + "\nNew Location = " + str(new_loc) + "\nYour Solution: " + str(
        move_ship(part5_board, cur_loc, new_loc)))
    print("Board:\n" + str(part5_board))
    print("move_ability: " + str(part5_board.move_ability))
    print()
    part5_board = Board(6, 7)
    part5_board.cells[2][2] = SHIP
    part5_board.cells[3][3] = SHIP
    part5_board.cells[0][0] = SHIP
    cur_loc = (3, 3)
    new_loc = (7, 6)
    print("Testing move_ship() with\nPlayer Board:\n" + str(part5_board) + "Current Location = " + str(
        cur_loc) + "\nNew Location = " + str(new_loc) + "\nYour Solution: " + str(
        move_ship(part5_board, cur_loc, new_loc)))
    print("Board:\n" + str(part5_board))
    print("move_ability: " + str(part5_board.move_ability))
    print()
    part5_board = Board(5, 5)
    part5_board.cells[2][2] = SHIP
    part5_board.cells[3][3] = SHIP
    part5_board.cells[0][0] = SHIP
    cur_loc = (2, 2)
    new_loc = (5, 5)
    print("Testing move_ship() with\nPlayer Board:\n" + str(part5_board) + "Current Location = " + str(
        cur_loc) + "\nNew Location = " + str(new_loc) + "\nYour Solution: " + str(
        move_ship(part5_board, cur_loc, new_loc)))
    print("Board:\n" + str(part5_board))
    print("move_ability: " + str(part5_board.move_ability))
    print()
    print("PART 6: ")
    part6_board_defender = Board(4, 6)
    part6_board_defender.cells[2][2] = SHIP
    part6_board_defender.cells[3][3] = BOMB
    part6_board_defender.cells[0][0] = SHIP
    part6_board_attacker = Board(4, 6)
    print("Testing air_strike() with\nDefender Board:\n" + str(
        part6_board_defender) + "\nCol = 3 \nYour Solution: " + str(
        air_strike(part6_board_attacker, part6_board_defender, 3)))
    print("Defender Board:\n" + str(part6_board_defender))
    print("Attacker air_strike_ability: " + str(part6_board_attacker.air_strike_ability))
    print()
    part6_board_defender = Board(6, 7)
    part6_board_defender.cells[2][2] = SHIP
    part6_board_defender.cells[3][3] = BOMB
    part6_board_defender.cells[0][0] = SHIP
    part6_board_attacker = Board(4, 6)
    print("Testing air_strike() with\nDefender Board:\n" + str(
        part6_board_defender) + "\nCol = 6 \nYour Solution: " + str(
        air_strike(part6_board_attacker, part6_board_defender, 6)))
    print("Defender Board:\n" + str(part6_board_defender))
    print("Attacker air_strike_ability: " + str(part6_board_attacker.air_strike_ability))
    print()
    part6_board_defender = Board(6, 7)
    part6_board_defender.cells[2][2] = SHIP
    part6_board_defender.cells[3][3] = BOMB
    part6_board_defender.cells[0][0] = SHIP
    part6_board_attacker = Board(4, 6)
    print("Testing air_strike() with\nDefender Board:\n" + str(
        part6_board_defender) + "\nCol = 8 \nYour Solution: " + str(
        air_strike(part6_board_attacker, part6_board_defender, 8)))
    print("Defender Board:\n" + str(part6_board_defender))
    print("Attacker air_strike_ability: " + str(part6_board_attacker.air_strike_ability))
