# -----------------------------------------------------------
# Definition of Game class that represents a game object along with it's values like the start time of the game from
# which the whole play time will be generated later after the solution is found. Another values are: the strategy given
# by the user when executing the program, the strategy method which is permutation of letters [L, R, U, D] or the short
# name of the heuristic of A-star algorithm, also the name of solution file and additional file are given so that they
# could be generated later.
# -----------------------------------------------------------

from Algorithms import *
from Board import Board
from copy import deepcopy


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
        """
        Starting the timer and the game with selected strategy and strategy method
        """

        if self.strategy == 'bfs':
            # Finding the solution using breadth-first search algorithm
            return bfs(self.start_time, self.strategy_method, self.initial_board)
        elif self.strategy == 'dfs':
            # Finding the solution using depth-first search algorithm
            return dfs(self.start_time, self.strategy_method, self.initial_board)
        else:
            # Finding the solution using A-star algorithm (either with Hamming or Manhattan heuristic)
            return astr(self.start_time, self.strategy_method, self.initial_board)

    def create_solution_file(self, solved, path):
        """
        Creating the solution file that contains
        the length of the list of moves that led to solution,
        moves one by one represented by the first letters of directions that were used to created all children until
        the solution was found.
        If no solution was found, only the "-1" value is written to the file.
        """

        f = open(self.solution_file_name, 'w+')
        if solved:
            f.write(str(len(path)))
            f.write('\n')
            for move in path:
                f.write(str(move).upper())
            f.write('\n')
        else:
            f.write("-1\n")
        f.close()

    def create_additional_file(self, solved, path, visited_nodes, processed_nodes,
                               depth_level, processing_time):
        """
        Creating the additional file that contains
        the path that led to solution (as in solution file),
        visited nodes which is the number of nodes that children was generated for,
        processed nodes which is the value of children that were generated,
        depth level which is the maximum depth of recursion,
        processing time which is the period of time the program worked for until the solution was found
        If no solution was found, only the "-1" value is written to the file.
        """

        f = open(self.additional_file_name, 'w+')
        if solved:
            f.write(str(len(path)))
            f.write('\n')
            f.write(str(visited_nodes))
            f.write('\n')
            f.write(str(processed_nodes))
            f.write('\n')
            f.write(str(depth_level))
            f.write('\n')
            f.write(str(round((processing_time) * 1000, 3)))
            f.write('\n')
        else:
            f.write("-1\n")
        f.close()
