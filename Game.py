import copy
import time
from Algorithms import *
from Board import Board


class Game:
    def __init__(self, strategy, strategy_method, start_file_name, solution_file_name, additional_file_name):
        self.start_time = time()
        self.strategy = strategy
        self.strategy_method = strategy_method
        self.solution_file_name = solution_file_name
        self.additional_file_name = additional_file_name

        # Creating the BOARD object along with reading the lines from input file and settings coordinates of empty fields
        # board = Board("4x4_01_0001.txt")
        self.initial_board = Board(start_file_name=start_file_name)
        # print(board)
        # print("Empty fields coordinates:", board.empty_field_coordinates)
        self.current_board = deepcopy(self.initial_board)

    def solve_game(self):
        if self.strategy == 'bfs':
            # Finding the solution using breadth-first search algorithm
            return bfs(self.start_time, self.initial_board)
        elif self.strategy == 'dfs':
            # Finding the solution using depth-first search algorithm
            return dfs(self.start_time, self.initial_board)
        else:
            # Finding the solution using A-star algorithm (either with Hamming or Manhattan heuristic)
            return astr(self.start_time, self.strategy_method, self.initial_board)

    def create_solution_file(self, solved, path):
        f = open(self.solution_file_name, 'w+')
        if solved:
            f.write(len(path))
            f.write('\n')
            f.write(path)
            f.write('\n')
        else:
            f.write("-1\n")
        f.close()

    def create_additional_file(self, solved, path, visited_nodes, processed_nodes,
                               depth_level, processing_time):
        f = open(self.additional_file_name, 'w+')
        if solved:
            f.write(len(path))
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
