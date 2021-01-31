# Sudoku Solver
### Python Sudoku Solver

Two different sudoku solvers are presented. The first is based on simple backtracking in a seqeuntial manner that goes through each blank in order (from top left to bottom right).

The second solver searches the entire sudoku to find the blank with the least number of possible answers and prioritizes filling this block. The order of backtracking is not from corner to corner, but based on having least number of probable answers (or greatest chance of guessing correct).

### How to use

Both solvers are present in the `Solver` class.
The sudoku to be input is a 2-D `numpy` array where the blanks are represented by `0`. The sudoku is modified in-situ and can be read as the output.

The following is an example of how to input the sudoku. The particular puzzle chosen is:
```
5 3 0 | 0 7 0 | 0 0 0 
6 0 0 | 1 9 5 | 0 0 0 
0 9 8 | 0 0 0 | 0 6 0 
---------------------
8 0 0 | 0 6 0 | 0 0 3 
4 0 0 | 8 0 3 | 0 0 1 
7 0 0 | 0 2 0 | 0 0 6 
---------------------
0 6 0 | 0 0 0 | 2 8 0 
0 0 0 | 4 1 9 | 0 0 5 
0 0 0 | 0 8 0 | 0 7 9 
```
Input it as a numpy array as follows:
```
sample = numpyp.array([[5,3,0,0,7,0,0,0,0],
                       [6,0,0,1,9,5,0,0,0],
                       [0,9,8,0,0,0,0,6,0],
                       [8,0,0,0,6,0,0,0,3],
                       [4,0,0,8,0,3,0,0,1],
                       [7,0,0,0,2,0,0,0,6],
                       [0,6,0,0,0,0,2,8,0],
                       [0,0,0,4,1,9,0,0,5],
                       [0,0,0,0,8,0,0,7,9]])
```
Declare and assign the input sudoku as follows
```
S = Solver()
S.F = sample
```
Invoke the first solver or the second solver as follows
```
S.solve1() #Solver 1
S.solve2() #Solver 2
```
The solved sudoku is stored in the member array `F` and can be displayed using `S.display()`

To print the intermediate values use `S.debug(True)` or `S.DEBUG=True`

`S.num_guesses` gives the number of total 'guesses' (correct + incorrect) made by the solvers.

The file *run_solver.py* gives an example of how to use both solvers 

 