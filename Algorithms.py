def dfs(start_time, board):
    visited_nodes = 0
    processed_nodes = 0
    depth_level = 0
    processing_time = 0
    solved = False

    pass

    return visited_nodes, processed_nodes, depth_level, processing_time, solved


def bfs(start_time, board):
    visited_nodes = 0
    processed_nodes = 0
    depth_level = 0
    processing_time = 0
    solved = False

    pass

    return visited_nodes, processed_nodes, depth_level, processing_time, solved


def astr(start_time, heuristic, board):
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


