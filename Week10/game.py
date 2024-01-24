import numpy as np

class ConnectFour:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.player_turn = 1

    def display_board(self):
        for row in reversed(range(self.rows)):
            print("|", end="")
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    print(" ", end="|")
                else:
                    print("X" if self.board[row][col] == 1 else "O", end="|")
            print()
        print("-" * (self.cols * 2 - 1))

    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.board[self.rows - 1][col] == 0

    def make_move(self, col):
        for row in range(self.rows):
            if self.board[row][col] == 0:
                self.board[row][col] = self.player_turn
                break

    def switch_player(self):
        self.player_turn = 3 - self.player_turn  # Switch between player 1 and player 2

    def check_winner(self, player):
        # Check horizontally
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True

        # Check vertically
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True

        # Check diagonally (from bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True

        # Check diagonally (from top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

        return False

    def is_board_full(self):
        return not any(0 in row for row in self.board)

    def evaluate(self):
        if self.check_winner(1):
            return 10
        elif self.check_winner(2):
            return -10
        else:
            return 0

    def minimax(self, depth, alpha, beta, maximizing_player):
        score = self.evaluate()

        if depth == 0 or abs(score) == 10 or self.is_board_full():
            return score

        if maximizing_player:
            max_eval = float('-inf')
            for col in range(self.cols):
                if self.is_valid_move(col):
                    self.make_move(col)
                    eval = self.minimax(depth - 1, alpha, beta, False)
                    self.board[self.get_next_empty_row(col) - 1][col] = 0  # Undo the move
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float('inf')
            for col in range(self.cols):
                if self.is_valid_move(col):
                    self.make_move(col)
                    eval = self.minimax(depth - 1, alpha, beta, True)
                    self.board[self.get_next_empty_row(col) - 1][col] = 0  # Undo the move
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    def get_next_empty_row(self, col):
        for row in range(self.rows):
            if self.board[row][col] == 0:
                return row + 1
        return self.rows  # If the column is full, return the bottom row index

    def get_best_move(self):
        best_move = -1
        best_val = float('-inf')
        for col in range(self.cols):
            if self.is_valid_move(col):
                self.make_move(col)
                move_val = self.minimax(4, float('-inf'), float('inf'), False)
                self.board[self.get_next_empty_row(col) - 1][col] = 0  # Undo the move
                if move_val > best_val:
                    best_val = move_val
                    best_move = col
        return best_move

def play_connect_four():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    connect_four = ConnectFour(rows, cols)

    while True:
        connect_four.display_board()
        if connect_four.player_turn == 1:
            col = int(input("Player 1, enter your move (column number): ")) - 1
        else:
            col = connect_four.get_best_move()

        if connect_four.is_valid_move(col):
            connect_four.make_move(col)
            if connect_four.check_winner(connect_four.player_turn):
                connect_four.display_board()
                print(f"Player {connect_four.player_turn} wins!")
                break
            elif connect_four.is_board_full():
                connect_four.display_board()
                print("It's a draw!")
                break
            else:
                connect_four.switch_player()
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_connect_four()



# # Imports

# from IPython.display import display, HTML, clear_output
# import random
# import time

# # Game Constants

# ROWS       = 6
# COLUMNS    = 7

# PIECE_NONE = ' '
# PIECE_ONE  = 'x'
# PIECE_TWO  = 'o'

# PIECE_COLOR_MAP = {
#     PIECE_NONE : 'white',
#     PIECE_ONE  : 'black',
#     PIECE_TWO  : 'red',
# }

# DIRECTIONS = (
#     (-1, -1), (-1, 0), (-1, 1),
#     ( 0, -1),          ( 0, 1),
#     ( 1, -1), ( 1, 0), ( 1, 1),
# )

# # Board Functions

# def create_board(rows=ROWS, columns=COLUMNS):
#     ''' Creates empty Connect 4 board '''
#     board = []

#     for row in range(rows):
#         board_row = []
#         for column in range(columns):
#             board_row.append(PIECE_NONE)
#         board.append(board_row)

#     return board

#   # Copy board

# def copy_board(board):
#     rows    = len(board)
#     columns = len(board[0])
#     copied  = create_board(rows, columns)

#     for row in range(rows):
#         for column in range(columns):
#             copied[row][column] = board[row][column]
#     return copied

# def print_board(board):
#     ''' Prints Connect 4 board '''
#     for row in board:
#         print ('|' + '|'.join(row) + '|')

# def drop_piece(board, column, piece):
#     ''' Attempts to drop specified piece into the board at the
#     specified column

#     If this succeeds, return True, otherwise return False.
#     '''

#     for row in reversed(board):
#         if row[column] == PIECE_NONE:
#             row[column] = piece
#             return True

#     return False

# def find_winner(board, length=4):
#     ''' Return whether or not the board has a winner '''

#     rows    = len(board)
#     columns = len(board[0])

#     for row in range(rows):
#         for column in range(columns):
#             if board[row][column] == PIECE_NONE:
#                 continue

#             if check_piece(board, row, column, length):
#                 return board[row][column]

#     return None

# def check_piece(board, row, column, length):
#     ''' Return whether or not there is a winning sequence starting from
#     this piece
#     '''
#     rows    = len(board)
#     columns = len(board[0])

#     for dr, dc in DIRECTIONS:
#         found_winner = True

#         for i in range(1, length):
#             r = row + dr*i
#             c = column + dc*i

#             if r not in range(rows) or c not in range(columns):
#                 found_winner = False
#                 break

#             if board[r][c] != board[row][column]:
#                 found_winner = False
#                 break

#         if found_winner:
#             return True

#     return False

# # HTML/SVG Functions

# def display_html(s):
#     ''' Display string as HTML '''
#     display(HTML(s))

# def create_board_svg(board, radius):
#     ''' Return SVG string containing graphical representation of board '''

#     rows     = len(board)
#     columns  = len(board[0])
#     diameter = 2*radius

#     svg  = '<svg height="{}" width="{}">'.format(rows*diameter, columns*diameter)
#     svg += '<rect width="100%" height="100%" fill="blue"/>'

#     for row in range(rows):
#         for column in range(columns):
#             piece = board[row][column]
#             color = PIECE_COLOR_MAP[piece]
#             cx    = column*diameter + radius
#             cy    = row*diameter + radius
#             svg += '<circle cx="{}" cy="{}" r="{}" fill="{}"/>'.format(cx, cy, radius*.75, color)

#     svg += '</svg>'

#     return svg
# # Here are two initial players you can use to test your bot:

# def HumanPlayer(board, history, players):
#     ''' Read move from human player '''
#     columns = len(board[0])
#     column  = -1

#     while column not in range(0, columns):
#         column = input('Which column? ')

#     return column

# def RandomPlayer(board, history, players):
#     ''' Randomly select a column '''
#     columns = len(board[0])
#     return random.randint(0, columns - 1)


# # Globals

# Players = (PIECE_ONE, PIECE_TWO)
# History = []
# Board   = create_board()
# Radius  = 40
# Winner  = None
# Tries   = 0

# # Game Loop

# while not Winner:
#     turn = len(History)

#     if turn % 2 == 0:
#         move = HumanPlayer(Board, History, Players)   # Player One
#     else:
#         move = RandomPlayer(Board, History, Players)  # Player Two

#     if drop_piece(Board, move, Players[turn % 2]):
#         Tries = 0
#         History.append(move)

#     if Tries > 3:
#         print ('Player {} is stuck!'.format((turn % 2) + 1))
#         break

#     clear_output()
#     display_html(create_board_svg(Board, Radius))

#     time.sleep(1)

#     Winner = find_winner(Board)

# print ('The Winner is {}'.format(PIECE_COLOR_MAP[Winner]))

# def BotPlayer(board, history, players):
#     '''
#     This is your AI bot player.  It is given the following arguments:

#         Board:    This is the current board.
#         History:  This is the history of the previous moves (columns).
#         Players:  This is the list of players.

#     Your function must not modify any of these objects.

#     After analyzing the inputs, your bot should return the column that
#     represents the best possible move.
#     '''