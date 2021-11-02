def start_game(board):
    pass


def game_ended(board):
    for solved_board in board.solved_boards:
        if solved_board == board.board:
            return True

    return False
