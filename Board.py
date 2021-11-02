class Board:
    row_count = 0
    column_count = 0
    coordinates_of_empty_field = {}
    board = []
    solved_board_3_3 = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '0']]
    solved_board_4_4 = [['1', '2', '3', '4'],
                        ['5', '6', '7', '8'],
                        ['9', '10', '11', '12'],
                        ['13', '14', '15', '0']]
    solved_boards = [solved_board_3_3, solved_board_4_4]

    def __init__(self, start_file_name):
        self.load_start_board(start_file_name)

    def load_start_board(self, start_file_name):
        f = open(start_file_name, "r")
        lines = f.readlines()
        lines = lines[1:-1]
        for line in lines:
            self.board.append(line)


