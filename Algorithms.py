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

    visited_nodes = 0
    processed_nodes = 0
    depth_level = 0
    processing_time = 0
    solved = False

    pass

    return visited_nodes, processed_nodes, depth_level, processing_time, solved


def astr(start_time, strategy_method, board):
    orders = [['R', 'D', 'U', 'L'],
              ['R', 'D', 'L', 'U'],
              ['D', 'R', 'U', 'L'],
              ['D', 'R', 'L', 'U'],
              ['L', 'U', 'D', 'R'],
              ['L', 'U', 'R', 'D'],
              ['U', 'L', 'D', 'R'],
              ['U', 'L', 'R', 'D']]

    visited_nodes = 0
    processed_nodes = 0
    depth_level = 0
    processing_time = 0
    solved = False

    if strategy_method == 'manh':
        pass
    else:
        pass

    return visited_nodes, processed_nodes, depth_level, processing_time, solved
