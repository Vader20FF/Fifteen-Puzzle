from queue import Queue
from copy import deepcopy
from time import time


def is_game_solved(board):
    solved_board_3_3 = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '0']]

    solved_board_4_4 = [['1', '2', '3', '4'],
                        ['5', '6', '7', '8'],
                        ['9', '10', '11', '12'],
                        ['13', '14', '15', '0']]

    solved_boards_examples = [solved_board_3_3, solved_board_4_4]

    for solved_board in solved_boards_examples:
        if board == solved_board:
            return True
    return False


def bfs(start_time, board):
    visited_nodes = 1
    processed_nodes = 1
    depth_level = 0

    path = []
    searched = [board.board]
    queue = [board]

    while queue:
        if is_game_solved(queue[0].board):
            solved = True
            processing_time = time() - start_time
            return path, visited_nodes, processed_nodes, depth_level, processing_time, solved

        for move in ['L', 'R', 'U', 'D']:
            queue[0].make_move(move)

        for child in queue[0].children:
            if child.board not in searched:
                path.append(child.last_move)
                searched.append(child.board)
                queue.append(child)
                processed_nodes += 1
        visited_nodes += 1

        queue.pop(0)

        print("BOARD:")
        print(board)
        print()
        print("BOARD CHILDREN:", len(board.children))
        print("QUEUE CHILDREN:", len(queue))
        print("PROCESSED NODES:", processed_nodes)
        counter = 1
        for child in queue:
            print("IN QUEUE CHILD NR:", counter)
            print(child)
            counter += 1
        print()
        print("----------------------------------")

    solved = False
    processing_time = time() - start_time
    return path, visited_nodes, processed_nodes, depth_level, processing_time, solved


def dfs(start_time, board):
    max_depth_level = 20

    visited_nodes = 0
    processed_nodes = 0
    depth_level = 0
    processing_time = 0
    solved = False

    pass

    return visited_nodes, processed_nodes, depth_level, processing_time, solved


def astr(start_time, heuristic, board):
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

    if heuristic == 'manh':
        pass
    else:
        pass

    return visited_nodes, processed_nodes, depth_level, processing_time, solved


def game_ended(board):
    for solved_board in board.solved_boards_examples:
        if solved_board == board.board:
            return True

    return False


