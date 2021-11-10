# -----------------------------------------------------------
# Implementations of different algorithms used to find the solution for the game
# -----------------------------------------------------------

from time import time


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
            print("SOLVED BOARD:")
            print(queue[0])
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
                # Adding the move, that leads to created current child, to the whole path
                path.append(child.last_move)
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

                for move in strategy_method_list:
                    board.make_move(move)

                for child in board.children:
                    path.append(child.last_move)
                    processed_nodes += 1
                    visited_nodes += 1
                    return dfs_recursion(searched, child, depth_level, visited_nodes, processed_nodes,
                                         strategy_method_list, solved)

    return dfs_recursion(searched, board, depth_level, visited_nodes, processed_nodes, strategy_method_list, False)


def astr(start_time, strategy_method, board):
    visited_nodes = 0
    processed_nodes = 0
    depth_level = 0
    processing_time = 0
    solved = False

    def get_index_of_field(board, field_value):
        for index_of_row, row in enumerate(board):
            for index_of_column, column_value in enumerate(row):
                if column_value == field_value:
                    return index_of_row, index_of_column

    if strategy_method == 'hamm':
        def calculate_distance(current_board, solved_board):
            distance = 0
            for index_of_row, row in enumerate(current_board):
                for index_of_column, elem in enumerate(row):
                    goal_row, goal_column = get_index_of_field(solved_board, elem)
                    if abs(index_of_row - goal_row) + abs(index_of_column - goal_column) != 0:
                        distance += 1
            return distance

    else:
        def calculate_distance(current_board, solved_board):
            distance = 0
            for index_of_row, row in enumerate(current_board):
                for index_of_column, elem in enumerate(row):
                    goal_row, goal_column = get_index_of_field(solved_board, elem)
                    distance += abs(index_of_row - goal_row) + abs(index_of_column - goal_column)
            return distance






    return visited_nodes, processed_nodes, depth_level, processing_time, solved
