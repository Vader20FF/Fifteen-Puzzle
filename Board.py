import time
from copy import deepcopy


class Board:
    row_count = 0
    column_count = 0
    empty_field_coordinates = {}
    children = {}
    board = []

    def __init__(self, start_file_name=None, board=None, parent=None, last_move=None, path=None, queue=None):
        if start_file_name is not None:
            self.load_start_board(start_file_name)
            self.row_count = len(board)
            self.column_count = len(board[0])
            self.initial_board = deepcopy(self.board)
        else:
            self.board = board
            self.row_count = len(board)
            self.column_count = len(board[0])
            self.parent = parent
            self.last_move = last_move
            self.path = deepcopy(path)
            self.queue = queue

        self.identify_empty_field_coordinates()

    def __repr__(self):
        for board in [self.initial_board, self.board]:
            if board == self.initial_board:
                print("Initial Board:")
            else:
                print("Current Board:")
            for row in range(int(self.row_count)):
                if row != 0:
                    print()
                for column in range(int(self.column_count)):
                    print(board[row][column] + " ", end="")
            print()
            print()

        return ""

    def load_start_board(self, start_file_name):
        f = open(f"start_files/{start_file_name}", "r")
        lines = f.readlines()
        self.row_count = lines[0][0]
        self.column_count = lines[0][2]
        lines = lines[1:]
        for line in lines:
            formatted_line = line.rstrip().split()
            self.board.append(formatted_line)

    def identify_empty_field_coordinates(self):
        for row in range(int(self.row_count)):
            for column in range(int(self.column_count)):
                if self.board[row][column] == "0":
                    self.empty_field_coordinates['row'] = row
                    self.empty_field_coordinates['column'] = column

    def make_child(self, move, modified_board):
        child = Board(start_file_name=None, board=modified_board, parent=self, last_move=self.last_move, path=self.path,
                      queue=self.queue)
        self.children[move] = child

    def make_move(self, move):
        empty_field_row = self.board.empty_field_coordinates['row']
        empty_field_column = self.board.empty_field_coordinates['column']

        tmp_board = deepcopy(self.board)

        if move == 'L':
            # Saving the value of field on the left of 'empty field'
            tmp_value = tmp_board[empty_field_row][empty_field_column - 1]
            # Assigning 'empty field' to the field on the left of 'empty field'
            tmp_board[empty_field_row][empty_field_column - 1] = tmp_board[empty_field_row][empty_field_column]
            # Assigning saved, previous value of field on the left to previous 'empty field' field
            tmp_board[empty_field_row][empty_field_column] = tmp_value
            # Changing the coordinates of 'empty field' field
            self.empty_field_coordinates['column'] -= 1
            self.make_child(move, tmp_board)
        elif move == 'R':
            # Saving the value of field on the right of 'empty field'
            tmp_value = tmp_board[empty_field_row][empty_field_column + 1]
            # Assigning 'empty field' to the field on the right of 'empty field'
            tmp_board[empty_field_row][empty_field_column + 1] = tmp_board[empty_field_row][empty_field_column]
            # Assigning saved, previous value of field on the right to previous 'empty field' field
            tmp_board[empty_field_row][empty_field_column] = tmp_value
            # Changing the coordinates of 'empty field' field
            self.empty_field_coordinates['column'] += 1
        elif move == 'U':
            # Saving the value of field above 'empty field'
            tmp_value = tmp_board[empty_field_row - 1][empty_field_column]
            # Assigning 'empty field' to the field above 'empty field'
            tmp_board[empty_field_row - 1][empty_field_column] = tmp_board[empty_field_row][empty_field_column]
            # Assigning saved, previous value of field above previous 'empty field' field
            tmp_board[empty_field_row][empty_field_column] = tmp_value
            # Changing the coordinates of 'empty field' field
            self.empty_field_coordinates['row'] -= 1
        elif move == 'D':
            # Saving the value of field under 'empty field'
            tmp_value = tmp_board[empty_field_row + 1][empty_field_column]
            # Assigning 'empty field' to the field under 'empty field'
            tmp_board[empty_field_row + 1][empty_field_column] = tmp_board[empty_field_row][empty_field_column]
            # Assigning saved, previous value of field under previous 'empty field' field
            tmp_board[empty_field_row][empty_field_column] = tmp_value
            # Changing the coordinates of 'empty field' field
            self.empty_field_coordinates['row'] += 1

    def remove_empty_moves(self):
        self.identify_empty_field_coordinates()

        if self.empty_field_coordinates['column'] == self.column_count - 1 and \
                self.empty_field_coordinates['row'] == self.row_count - 1:
            self.queue.remove('R')
            self.queue.remove('D')
        elif self.empty_field_coordinates['column'] == self.column_count - 1 and \
                self.empty_field_coordinates['row'] == 0:
            self.queue.remove('R')
            self.queue.remove('U')
        elif self.empty_field_coordinates['column'] == 0 and \
                self.empty_field_coordinates['row'] == 0:
            self.queue.remove('L')
            self.queue.remove('U')
        elif self.empty_field_coordinates['column'] == 0 and \
                self.empty_field_coordinates['row'] == self.row_count - 1:
            self.queue.remove('L')
            self.queue.remove('D')
        elif self.empty_field_coordinates['column'] == 0:
            self.queue.remove('L')
        elif self.empty_field_coordinates['column'] == self.column_count - 1:
            self.queue.remove('R')
        elif self.empty_field_coordinates['row'] == 0:
            self.queue.remove('U')
        elif self.empty_field_coordinates['row'] == self.row_count - 1:
            self.queue.remove('D')
