import random

from course_project import *


def generate_ai_cell_locations(board):
    positions = []
    for i in range(board.num_rows):
        for j in range(board.num_cols):
            positions.append((i + 1, j + 1))
    return positions


def ai_take_turn(possible_ai_squares, human_player):
    loc = random.choice(possible_ai_squares)
    possible_ai_squares.remove(loc)
    print('Computer attacks you at position (' + str(loc[0]) + ', ' + str(loc[1]) + ')!')
    attack(human_player, loc[0], loc[1])
    return possible_ai_squares


# Main program
if __name__ == '__main__':
    game = Game(Board(4, 6), Board(4, 6))  # computer player, human player

    print('Welcome to BATTLESHIP: CSE 101 Edition!\n')
    print('Choose where your three battleships will go.')
    ships_placed = 0
    while ships_placed < 3:
        r = int(input('Enter row # where you want to place ship #' + str(1 + ships_placed) + ': '))
        c = int(input('Enter column # where you want to place ship #' + str(1 + ships_placed) + ': '))

        if not is_valid_location(game.player_board, r, c):
            print('Invalid location. Try again.')
        else:
            success = place_ship(game.player_board, r, c)
            if success:
                print('Ship #' + str(1 + ships_placed) + ' placed.\n')
                ships_placed += 1
            else:
                print('A ship was already placed at that location. Try again.\n')

    # Place computer player's ships
    ai_cells = generate_ai_cell_locations(game.ai_board)
    computer_ships = random.sample(ai_cells, 3)
    for ship in computer_ships:
        place_ship(game.ai_board, ship[0], ship[1])

    print(game)
    game_over = False
    while not game_over:
        print('Player\'s turn.')
        if game.player_board.air_strike_ability:
            air = input('Do you want to use air-strike? Y/N? ')
            if air.upper() == 'Y':
                c = int(input('Enter column # you want to use air strike on: '))
                if is_valid_location(game.ai_board, 1, c):
                    air_strike(game.player_board, game.ai_board, c)
                else:
                    print('Invalid column to airstrike. You lose your turn!')

                print('\nComputer player\'s turn.')
                ai_cells = ai_take_turn(ai_cells, game.player_board)
                print(game)
                if game_status(game.player_board, game.ai_board) == PLAYER_LOST:
                    print('You have been defeated!')
                    game_over = True
                continue

        if game.player_board.move_ability:
            move = input('Do you want to move one of your ships Y/N? ')
            if move.upper() == 'Y':
                curr_row = int(input('Enter row # of the ship you want to move: '))
                curr_col = int(input('Enter column # of the ship you want to move: '))
                new_row = int(input('Enter new row # of the ship: '))
                new_col = int(input('Enter new column # of the ship: '))
                if not is_valid_location(game.player_board, curr_row, curr_col) or \
                        not is_valid_location(game.player_board, new_row, new_col):
                    print('Illegal move...You lose your turn!')

                success = move_ship(game.player_board, (curr_row, curr_col), (new_row, new_col))
                if not success:
                    print('Illegal move...You lose your turn!')

                print('\nComputer player\'s turn.')
                ai_cells = ai_take_turn(ai_cells, game.player_board)
                print(game)
                if game_status(game.player_board, game.ai_board) == PLAYER_LOST:
                    print('You have been defeated!')
                    game_over = True
                continue

        valid_move = False
        while not game_over and not valid_move:
            r = int(input('Enter row # you want to attack: '))
            c = int(input('Enter column # you want to attack: '))
            if is_valid_location(game.ai_board, r, c) and attack(game.ai_board, r, c):
                valid_move = True
            else:
                print('Illegal move, try again.')

        print(game)
        if game_status(game.player_board, game.ai_board) == COMPUTER_LOST:
            print('You won the game!')
            game_over = True
        elif game_status(game.player_board, game.ai_board) == PLAYER_LOST:
            print('You have been defeated!')
            game_over = True
        else:
            print('\nComputer player\'s turn: ')
            ai_cells = ai_take_turn(ai_cells, game.player_board)
            print(game)
            if game_status(game.player_board, game.ai_board) == PLAYER_LOST:
                print('You have been defeated!')
                game_over = True
