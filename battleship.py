EMPTY = u"\u25A1"  # A white square
FOG = u"\u25A0"  # A black square
EXPLORED = u"\u2612"  # A square with an X inside
BOMB = u"\u25CE"  # Two concentric circles
SHIP = u"\u26F5"  # An icon of a sailboat

PLAYER_LOST = 100
COMPUTER_LOST = 200


class Game:
    def __init__(self, player_board, ai_board):
        self.ai_board = ai_board
        self.player_board = player_board

    def __repr__(self):
        board = self.ai_board
        board_repr = 'Attacks you made against computer player:\n'

        for i in range(board.num_rows):
            for j in range(board.num_cols):
                if board.cells[i][j] == SHIP:
                    board_repr += FOG + ' '
                else:
                    if board.cells[i][j] == EMPTY:
                        board_repr += FOG + ' '
                    else:
                        board_repr += board.cells[i][j] + ' '
            board_repr += '\n'

        return board_repr + '\nYour board: \n' + str(self.player_board)


class Board:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cells = [[EMPTY for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.air_strike_ability = True
        self.move_ability = True

    def __repr__(self):
        board_repr = ''
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                board_repr += self.cells[i][j] + ' '
            board_repr += '\n'
        return board_repr

    def __eq__(self, other):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if self.cells[r][c] != other.cells[r][c]:
                    return False
        return True
