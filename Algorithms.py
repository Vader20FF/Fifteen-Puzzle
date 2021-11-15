# -----------------------------------------------------------
# Implementations of different algorithms used to find the solution for the game
# -----------------------------------------------------------
from random import random
from time import time


def get_solved_board_from_current_board(board):
    """
    Getting solved board from the given board
    """

    row_count = 0
    column_count = 0

    for row in range(len(board)):
        row_count += 1
        if row == 1:
            for column in range(len(board[row])):
                column_count += 1

    solved_board = []
    current_number = 1

    for row in range(row_count):
        solved_board.append([])
        for column in range(column_count):
            if row == row_count - 1 and column == column_count - 1:
                solved_board[row].append("0")
                continue
            solved_board[row].append(str(current_number))
            current_number += 1

    return solved_board


def is_game_solved(board):
    """
    Checking whether current board is solved so that every number from the left to the right and from up to down are
    in numerical order and the last number is 0. The solved board should look like these ones:

    [['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '0']]

    OR

    [['1', '2', '3', '4'],
    ['5', '6', '7', '8'],
    ['9', '10', '11', '12'],
    ['13', '14', '15', '0']]
    """

    solved = False

    if board[0][0] == "1":
        current_number = 1
        for row in range(len(board)):
            for column in range(len(board[row])):
                if row == (len(board) - 1) and column == (len(board[row]) - 1):
                    current_number = 0
                if board[row][column] != str(current_number):
                    return solved
                current_number += 1
        solved = True
        return solved
    else:
        return solved


def bfs(start_time, strategy_method, board):
    visited_nodes = 1
    processed_nodes = 1
    depth_level = 0

    strategy_method_list = list(strategy_method)

    # Creating the path list that will contain all the moves that lead to solution
    path = []
    # Creating the searched list that initially contains the initial board and another visited nodes will be added if
    # they are not the solution
    searched = [board.board]
    # Creating the queue that will contain all nodes across which the solution should be found
    queue = [board]

    # DEBUG - printing the initial board
    print()
    print("INITIAL BOARD:")
    print(board)
    # END DEBUG - printing the initial board

    while queue:
        # Checking if current first element (board) in queue meets the condition of solved board
        if is_game_solved(queue[0].board):
            # If it does, return with calculated values
            solved = True

            # DEBUG - printing the solved board
            print("SOLVED BOARD:")
            print(queue[0])
            # END DEBUG - printing the solved board

            while queue[0].parent is not None:
                # As the solution has been found, path is being restored that led to this solution going from
                # child to it's parent until the node is root and there is no parent
                path.append(queue[0].last_move)
                queue[0] = queue[0].parent
            path.reverse()

            processing_time = time() - start_time
            return path, visited_nodes, processed_nodes, depth_level, processing_time, solved

        # If no, go on with checking the moves that can be done with this board according to selected strategy_method
        for move in strategy_method_list:
            # Making the move with current board and creating it's children so that they can be checked and potentially
            # added to the queue
            queue[0].make_move(move)

        for child in queue[0].children:
            # For every created child check if it's board has not already been created earlier. Doing this by checking
            # if current board was added to searched boards earlier
            if child.board not in searched:
                # Adding the child's board to searched boards
                searched.append(child.board)
                # Incrementing processed nodes value to indicate that next child was checked and it's not the solution
                processed_nodes += 1
                # Checking if current selected child meets the condition of solved board
                if is_game_solved(child.board):
                    # If it does, return with calculated values
                    solved = True

                    # DEBUG - printing the solved board
                    print("SOLVED BOARD:")
                    print(child)
                    # END DEBUG - printing the solved board

                    path.clear()
                    while child.parent is not None:
                        # As the solution has been found, path is being restored that led to this solution going from
                        # child to it's parent until the node is root and there is no parent
                        path.append(child.last_move)
                        child = child.parent
                    path.reverse()

                    processing_time = time() - start_time
                    return path, visited_nodes, processed_nodes, depth_level, processing_time, solved
                # If no, add the child to the queue so that it's children could be created
                queue.append(child)

        # Incrementing visited nodes value to indicate that children were created for another node in queue
        visited_nodes += 1

        # DEBUG
        # print("BOARD:")
        # print(queue[0])
        # print("BOARD CHILDREN:", len(queue[0].children))
        # END DEBUG

        # Removing visited node from the queue
        queue.pop(0)

        # DEBUG
        # print("QUEUE BOARDS:", len(queue))
        # print("PROCESSED NODES:", processed_nodes)
        # print("VISITED NODES:", visited_nodes)
        #
        # counter = 1
        # for child in queue:
        #     print("QUEUE BOARD NR:", counter)
        #     print(child)
        #     counter += 1
        # print()
        # print("----------------------------------")
        # END DEBUG

    solved = False
    processing_time = time() - start_time
    return path, visited_nodes, processed_nodes, depth_level, processing_time, solved


def dfs(start_time, strategy_method, board):
    max_depth_level = 20

    visited_nodes = 1
    processed_nodes = 1
    depth_level = 0

    strategy_method_list = list(strategy_method)

    path = []
    searched = set()

    # DEBUG - printing the initial board
    print()
    print("INITIAL BOARD:")
    print(board)
    # END DEBUG - printing the initial board

    def dfs_recursion(searched, board, depth_level, visited_nodes, processed_nodes, strategy_method_list, solved):
        depth_level += 1

        if solved:
            processing_time = time() - start_time
            return path, visited_nodes, processed_nodes, depth_level, processing_time, True
        else:
            if is_game_solved(board.board):
                print("SOLVED BOARD:")
                print(board)
                processing_time = time() - start_time
                return path, visited_nodes, processed_nodes, depth_level, processing_time, True

            if depth_level == max_depth_level:
                processing_time = time() - start_time
                return path, visited_nodes, processed_nodes, depth_level, processing_time, False

            if board not in searched:
                searched.add(board)

                visited_nodes += 1

                for move in strategy_method_list:
                    board.make_move(move)

                for child in board.children:
                    path.append(child.last_move)
                    processed_nodes += 1
                    return dfs_recursion(searched, child, depth_level, visited_nodes, processed_nodes,
                                         strategy_method_list, solved)

    return dfs_recursion(searched, board, depth_level, visited_nodes, processed_nodes, strategy_method_list, False)


def astr(start_time, strategy_method, board):
    visited_nodes = 0
    processed_nodes = 0
    depth_level = 0

    # Creating the path list that will contain all the moves that lead to solution
    path = []

    moves_directions = ["L", "R", "U", "D"]

    # DEBUG - printing the initial board
    print()
    print("INITIAL BOARD:")
    print(board)
    # END DEBUG - printing the initial board

    def get_index_of_field(board, field_value):
        """
        Getting row and column number of the solved board from the given board and given field of this board
        """

        solved_board = get_solved_board_from_current_board(board)

        for index_of_row, row in enumerate(solved_board):
            for index_of_column, column_value in enumerate(row):
                if column_value == field_value:
                    return index_of_row, index_of_column

    def calculate_hamming_distance(current_board):
        """
        Getting the hamming distance from the field of the current board to the field of same value in the solved board
        """

        hamming_distance = 0
        for index_of_row, row in enumerate(current_board):
            for index_of_column, column_value in enumerate(row):
                goal_row_index, goal_column_index = get_index_of_field(current_board, column_value)
                if abs(index_of_row - goal_row_index) + abs(index_of_column - goal_column_index) != 0:
                    hamming_distance += 1
        return hamming_distance

    def calculate_manhattan_distance(current_board):
        """
        Getting the manhattan distance from the field of the current board to the field of same value in the solved
        board
        """

        manhattan_distance = 0
        for index_of_row, row in enumerate(current_board):
            for index_of_column, column_value in enumerate(row):
                goal_row_index, goal_column_index = get_index_of_field(current_board, column_value)
                manhattan_distance += abs(index_of_row - goal_row_index) + abs(index_of_column - goal_column_index)
        return manhattan_distance

    current_board = board
    child_errors = {}

    while True:
        child_errors.clear()

        # Checking if current first element (board) in queue meets the condition of solved board
        if is_game_solved(current_board.board):
            # If it does, return with calculated values
            solved = True
            processing_time = time() - start_time
            # DEBUG - printing the solved board
            print("SOLVED BOARD:")
            print(current_board)
            # END DEBUG - printing the solved board
            return path, visited_nodes, processed_nodes, depth_level, processing_time, solved
        else:
            # If no, go on with checking the moves that can be done with this board according to
            # selected strategy_method
            for move in moves_directions:
                # Making the move with current board and creating it's children so that they can be
                # checked and potentially added to the queue
                current_board.make_move(move)

            for child in current_board.children:
                processed_nodes += 1

                if strategy_method == "hamm":
                    child_errors[child] = calculate_hamming_distance(child.board)
                else:
                    child_errors[child] = calculate_manhattan_distance(child.board)

            min_error_value = min(child_errors.values())
            for key in child_errors:
                if child_errors[key] == min_error_value:
                    path.append(key.last_move)
                    current_board = key
                    break

            visited_nodes += 1

    # solved = False
    # processing_time = time() - start_time
    # return path, visited_nodes, processed_nodes, depth_level, processing_time, solved
