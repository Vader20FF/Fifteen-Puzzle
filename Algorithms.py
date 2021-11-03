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
    processing_time = 0
    solved = False

    searched = []
    queue = []

    while True:
        if is_game_solved(board.current_board):
            solved = True
            return board.path, visited_nodes, processed_nodes, depth_level, processing_time, solved
        else:
            if not board.last_move is None:
                board.remove_empty_moves()
            for move in board.queue:
                processed_nodes += 1
                board.make_move(move)
                board = board.children[move]
                queue.append(board)
                last_move = board.path[-1]
                board.identify_empty_field_coordinates()
                board = board.parent
            try:
                if board.last is not None:
                    queue.remove(board)
            except ValueError:
                pass
            board = queue[0]
            visited_nodes += 1
            board.identify_empty_field_coordinates()


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


