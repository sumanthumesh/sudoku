from sudoku import sudoku
import sys
import numpy as np

DEBUG = False

if(DEBUG == True):
    original_stdout = sys.stdout
    file = open("run_sudoku.log","w")
    sys.stdout = file                
S = sudoku()
#print(S.group(5,4))
            
sample = np.array([[1,7,2,5,4,9,6,8,3],
                    [6,4,5,8,7,3,2,1,9],
                    [3,8,9,2,6,1,7,4,5],
                    [4,9,6,3,2,7,8,5,1],
                    [8,1,3,4,5,6,9,7,2],
                    [2,5,7,1,9,8,4,3,6],
                    [9,6,4,7,1,5,3,2,8],
                    [7,3,1,6,8,2,5,9,4],
                    [5,2,8,9,3,4,1,6,7]])

#S.F = sample

#print(S.isInGroup(1, 3))
#print(S.isLegal(9,4,6))
S.debug(False)
S.generate()
#print("Finished")
if(DEBUG == True):
    sys.stdout = original_stdout
    file.close()
    
S.display()