# Fifteen-Puzzle

## Table of Content
* [General Info](#setup)
* [Technologies](#technologies)
* [How To Use](#how-to-use)
* [How It Works](#how-it-works)
* [Examples Of Use](#examples-of-use)

## General info
Fifteen Puzzle Python solver with implementation of AI alghorithms: breadth-first search, depth-first search, A-star (Hamming and Manhattan heuristics)

## Technologies
Python 3.10

## Status
Finished

## How To Use
#### The program can be executed like:

`python .\main.py bfs RDUL 4x4_01_00001.txt 4x4_01_00001_bfs_rdul_sol.txt 4x4_01_00001_bfs_rdul_stats.txt`

or

`python .\main.py dfs LUDR 4x4_01_00001.txt 4x4_01_00001_dfs_ludr_sol.txt 4x4_01_00001_dfs_ludr_stats.txt`

or

`python .\main.py astr manh 4x4_01_00001.txt 4x4_01_00001_astr_manh_sol.txt 4x4_01_00001_astr_manh_stats.txt`
    
#### Scheme:
`python .\main.py [strategy] [strategy_method] [start_file] [solution_file] [additional_file]`
    
#### Where:

[strategy] is one of [bfs, dfs, astr], 

[strategy_method] is one of [(letters L, R, U, D in any order), hamm, manh], 

[start_file] is the name of the file that the values of initial board are stored in,

[solution_file] is the name of the file that calculated values during the game are written to after the game is done,

[addition_file] is the name of the file that calculated values during the game are written to after the game is done

    
#### What's more:

bfs - finding the solution with breadth-first search algorithm

dfs - finding the solution with depth-first search algorithm

astr - finding the solution with a-star algorithm

hamm - Hamming heuristic

manh - Manhattan heuristic
    
permutation of letters L, R, U, D can only be applied to the bfs and dfs algorithm

hamm and manh heuristics can only be applied to the a-star algorithm


## How It Works
After the program execution in one of the ways explained in the 'How To Use' section, it will perform calculations and depending on the starting works, it will find the solution or not.
There will be to output files: solution_file and additional_file. They have structure as below:

#### solution_file:

line 1: the length of the list of moves that led to solution

line 2: moves one by one represented by the first letters of directions that were used to created all children until the solution was found


#### additional_file:

line 1: the path that led to solution (as in solution file)

line 2: visited nodes which is the number of nodes that children was generated for

line 3: processed nodes which is the value of children that were generated

line 4: depth level which is the maximum depth of recursion (only in dfs, for rest "0" value is written in the file)

line 5: processing time in miliseconds [ms], which is the period of time the program worked for until the solution was found



## Examples Of Use

`PS [YOUR DIRECTORY]\program> python .\main.py bfs rdul 4x4_04_00010.txt 4x4_04_00010_rdul_sol.txt 4x4_04_00010_rdul_stats.txt`

#### Console Output

![Algorithm schema](https://github.com/Vader20FF/Fifteen-Puzzle/blob/master/output_files_for_git/console_output.jpg)

#### Generated Solution File

![Algorithm schema](https://github.com/Vader20FF/Fifteen-Puzzle/blob/master/output_files_for_git/solution_file_output.jpg)

#### Generated Additional File

![Algorithm schema](https://github.com/Vader20FF/Fifteen-Puzzle/blob/master/output_files_for_git/additional_file_output.jpg)


