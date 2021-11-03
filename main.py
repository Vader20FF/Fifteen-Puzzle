# SISE 2021
# LABORATORY 1 - "FIFTEEN PUZZLE"

from Game import Game
import argparse

if __name__ == '__main__':
    # Parsing the arguments
    parser = argparse.ArgumentParser(description="strategy, strategy_method, start_file, solution_file, "
                                                 "additional_file.")
    parser.add_argument('strategy')
    parser.add_argument('strategy_method')
    parser.add_argument('start_file')
    parser.add_argument('solution_file')
    parser.add_argument('additional_file')
    args = parser.parse_args()

    # Creating and starting the GAME
    game = Game(args.strategy, args.strategy_method, args.start_file, args.solution_file, args.additional_file)

    path, visited_nodes, processed_nodes, depth_level, processing_time, solved = game.solve_game()

    game.create_solution_file(solved, path)
    game.create_additional_file(solved, path, visited_nodes, processed_nodes, depth_level, processing_time)

    # Wait until user presses key
    input("Press Enter to continue...")
