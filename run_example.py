from solver import Solver
import numpy as np

S = Solver()
            
sample = np.array([[5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]])

S.debug(False) #Don't print intermediate steps

#Solver1
print("Solver1")
S.F = sample
S.solve1()
S.display()#Display solver 1 result
print("Number of guesses "+ str(S.num_guesses))#Display solver1 number of guesses

#Solver2
print("\nSolver2")
S.F = sample
S.solve2()
S.display()#Display solver 2 result
print("Number of guesses "+ str(S.num_guesses))#Display solver2 number of guesses
