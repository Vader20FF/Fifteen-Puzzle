import copy
import time
from Algorithms import *


class Game:
    moves = []

    def __init__(self, strategy, strategy_method, solution_file_name, additional_file_name, board):
        self.start_time = time.time()
        self.strategy = strategy
        self.strategy_method = strategy_method
        self.solution_file_name = solution_file_name
        self.additional_file_name = additional_file_name
        self.board = board

        visited_nodes, processed_nodes, depth_level, processing_time, solved = self.solve_game()
        self.create_solution_file(solved)
        self.create_additional_file(solved, visited_nodes, processed_nodes, depth_level, processing_time)

    def solve_game(self):
        if self.strategy == 'bfs':
            # Finding the solution using breadth-first search algorithm
            return bfs(self.start_time, self.board)
        elif self.strategy == 'dfs':
            # Finding the solution using depth-first search algorithm
            return dfs(self.start_time, self.board)
        else:
            # Finding the solution using A-star algorithm (either with Hamming or Manhattan heuristic)
            return astr(self.start_time, self.strategy_method, self.board)



    def make_move(self, move):
        self.moves.append(move)
        self.board.make_move(move)

    def create_solution_file(self, solved):
        f = open(self.solution_file_name, 'w+')
        if solved:
            f.write(len(self.moves))
            f.write('\n')
            f.write(self.moves)
            f.write('\n')
        else:
            f.write("-1\n")
        f.close()

    def create_additional_file(self, solved, visited_nodes, processed_nodes,
                              depth_level, processing_time):
        f = open(self.additional_file_name, 'w+')
        if solved:
            f.write(len(self.moves))
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
