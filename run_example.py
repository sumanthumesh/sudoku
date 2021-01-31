from solver import Solver
import sys
import numpy as np
         
original_stdout = sys.stdout
file = open("run_solver.log","w")
sys.stdout = file

S = Solver()
#print(S.group(5,4))
            
sample = np.array([[5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]])

S.debug(False)
S.F = sample
S.solve2()
#print(S.isInGroup(1, 3))
#print(S.isLegal(9,4,6))
#print("Finished")
    




sys.stdout = original_stdout

S.display()
print(S.num_guesses)