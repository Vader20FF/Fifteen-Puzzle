import time


class Board:
    row_count = 0
    column_count = 0
    empty_field_coordinates = {}
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
        self.set_empty_field_coordinates()

    def load_start_board(self, start_file_name):
        f = open(start_file_name, "r")
        lines = f.readlines()
        print(lines)
        row_count = lines[0][0]
        column_count = lines[0][2]
        lines = lines[1:-1]
        for line in lines:
            formatted_line = line.rstrip().split()
            self.board.append(formatted_line)

    def create_solution_file(self, solution_file_name, solved, solution_length, moves):
        f = open(solution_file_name, 'w+')
        if solved:
            f.write(solution_length)
            f.write('\n')
            f.write(moves)
            f.write('\n')
        else:
            f.write("-1\n")
        f.close()

    def create_additional_file(self, additional_file_name, solved, solution_length, visited_nodes, processed_nodes,
                              depth_level, processing_time):
        f = open(additional_file_name, 'w+')
        if solved:
            f.write(solution_length)
            f.write('\n')
            f.write(visited_nodes)
            f.write('\n')
            f.write(processed_nodes)
            f.write('\n')
            f.write(depth_level)
            f.write('\n')
            f.write(str(round((time.time() - processing_time) * 1000, 3)))
            f.write('\n')
        else:
            f.write("-1\n")
        f.close()

    def set_empty_field_coordinates(self):
        for row in range(len(self.board)):
            for column in range(len(self.board) + 1):
                if self.board[row][column] == "0":
                    self.empty_field_coordinates = {row, column}



