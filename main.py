# SISE 2021
# LABORATORY 1 - "FIFTEEN PUZZLE"

from Game import Game
import argparse

if __name__ == '__main__':
    """ 
    The program can be executed like:
    python .\main.py bfs RDUL 4x4_01_00001.txt 4x4_01_00001_bfs_rdul_sol.txt 4x4_01_00001_bfs_rdul_stats.txt
    OR
    python .\main.py dfs LUDR 4x4_01_00001.txt 4x4_01_00001_dfs_ludr_sol.txt 4x4_01_00001_dfs_ludr_stats.txt
    OR
    python .\main.py astr manh 4x4_01_00001.txt 4x4_01_00001_astr_manh_sol.txt 4x4_01_00001_astr_manh_stats.txt
    
    SCHEME:
    python .\main.py [strategy] [strategy_method] [start_file] [solution_file] [additional_file]
    
    WHERE:
    [strategy] is one of [bfs, dfs, astr], 
    [strategy_method] is one of [(letters L, R, U, D in any order), hamm, manh], 
    [start_file] is the name of the file that the values of initial board are stored in,
    [solution_file] is the name of the file that calculated values during the game are written to after the game is done
    [addition_file] is the name of the file that calculated values during the game are written to after the game is done
    
    WHAT'S MORE:
    bfs - finding the solution with breadth-first search algorithm
    dfs - finding the solution with depth-first search algorithm
    astr - finding the solution with a-star algorithm
    hamm - Hamming heuristic
    manh - Manhattan heuristic
    
    permutation of letters L, R, U, D can only be applied to the bfs and dfs algorithm
    hamm and manh heuristics can only be applied to the a-star algorithm
    """

    parser = argparse.ArgumentParser(description="strategy, strategy_method, start_file, solution_file, "
                                                 "additional_file.")
    parser.add_argument('strategy')
    parser.add_argument('strategy_method')
    parser.add_argument('start_file')
    parser.add_argument('solution_file')
    parser.add_argument('additional_file')
    args = parser.parse_args()

    # Creating and starting the game
    game = Game(args.strategy, args.strategy_method, args.start_file, args.solution_file, args.additional_file)

    # Getting the game parameters after solving the game
    path, visited_nodes, processed_nodes, depth_level, processing_time, solved = game.solve_game()

    # Creating the solution file and additional file that contain game parameters
    game.create_solution_file(solved, path)
    game.create_additional_file(solved, path, visited_nodes, processed_nodes, depth_level, processing_time)

    # Wait until user presses key
    # input("Press Enter to continue...")
