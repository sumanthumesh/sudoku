import numpy as np
import random

class Solver:
    
    def debug(self,x):
        self.DEBUG=x
    
    def __init__(self):
        self.F = np.zeros(shape=(9,9),dtype=int)
        
    def display(self):
        for r in range(9):
            for c in range(9):
                print(str(self.F[r][c]) + ' ',end='')
                if(c==2 or c==5):
                    print("| ",end='')
            print()
            if(r==2 or r==5):
                print('---------------------')
                
    def group(self,r,c):
        if(r>=0 and r<=2):
            row=0
        elif(r>=3 and r<=5):
            row=1
        elif(r>=6 and r<=8):
            row=2
        if(c>=0 and c<=2):
            col=0
        elif(c>=3 and c<=5):
            col=1
        elif(c>=6 and c<=8):
            col=2
        return row * 3 + col
    
    def isInGroup(self,ele,group):
        if(group == 0):
            if(ele in self.F[0:0+3,0:0+3]):
                return True
        elif(group == 1):
            if(ele in self.F[0:0+3,3:3+3]):
                return True
        elif(group == 2):
            if(ele in self.F[0:0+3,6:6+3]):
                return True    
        elif(group == 3):
            if(ele in self.F[3:3+3,0:0+3]):
                return True
        elif(group == 4):
            if(ele in self.F[3:3+3,3:3+3]):
                return True
        elif(group == 5):
            if(ele in self.F[3:3+3,6:6+3]):
                return True
        elif(group == 6):
            if(ele in self.F[6:6+3,0:0+3]):
                return True
        elif(group == 7):
            if(ele in self.F[6:6+3,3:3+3]):
                return True
        elif(group == 8):
            if(ele in self.F[6:6+3,6:6+3]):
                return True
        return False
    
    def isLegal(self,ele,r,c):
        if(ele in self.F[r,:]):
            return False
        if(ele in self.F[:,c]):
            return False
        if(self.isInGroup(ele,self.group(r, c))):
            return False
        return True
    
    def allPossible(self,r,c):
        possibles = []
        for i in range(1,10):
            if(self.isLegal(i,r,c)):
                possibles.append(i)
        return possibles
    
    def choose(self,possibles,memory):
        random.shuffle(possibles)
        for x in possibles:
            if(not(x in memory)):
                return x
        return None
    
    def solve1(self):
        memory = []
        for i in range(81):
            memory.append([])
        stack = []
        stack.append([0,0])
        self.num_guesses = 0
        while (peek_stack(stack)[0] < 9 and peek_stack(stack)[1] < 9):
            current_pos = peek_stack(stack)
            r = current_pos[0]
            c = current_pos[1]
            if(self.DEBUG == True):
                print("Pos:("+str(r)+","+str(c)+")")
            if(self.F[r][c]==0):
                possibles = self.allPossible(r,c)
                if(self.DEBUG == True):
                    print("Possibles:",end='')
                    print(possibles)
                if(len(possibles) == 0):
                    temp = stack.pop()
                    temp = peek_stack(stack)
                    self.F[temp[0],temp[1]]=0
                    if(self.DEBUG == True):
                        print("Memory:",end='')
                        print(memory[two2one(r,c)])
                    memory[two2one(r,c)]=[]
                    if(self.DEBUG == True):
                        print("Popped:",end='')
                        print(temp)
                else:
                    if(self.DEBUG == True):
                        print("Memory:",end='')
                        print(memory[two2one(r,c)])
                    choice = self.choose(possibles,memory[two2one(r,c)])
                    if(choice == None):
                        temp = stack.pop()
                        temp = peek_stack(stack)
                        self.F[temp[0],temp[1]]=0
                        memory[two2one(r,c)]=[]
                        if(self.DEBUG == True):
                            print("Popped:",end='')
                            print(temp)
                    else:
                        self.F[r][c] = choice
                        if(self.DEBUG == True):
                            print("Choice:"+str(choice))
                        memory[two2one(r,c)].append(choice)
                        if(c!=8):
                            next_c = c + 1
                            next_r = r
                        else:
                            next_c = 0
                            next_r = r + 1
                        stack.append([next_r,next_c])
                        if(self.DEBUG == True):
                            print("Pushed:("+str(next_r)+","+str(next_c)+")")
                if(self.DEBUG == True):
                    self.display()

            else:
                stack.pop()
                if(c!=8):
                    next_c = c + 1
                    next_r = r
                else:
                    next_c = 0
                    next_r = r + 1
                stack.append([next_r,next_c])
                if(self.DEBUG == True):
                    print("Pushed:("+str(next_r)+","+str(next_c)+")")
            self.num_guesses += 1
            
    def checkBestCase(self):
        least_num_poss = 9
        best_poss = [-1,-1]
        for r in range(9):
            for c in range(9):
                if(self.F[r][c]==0):
                    possibilities = self.allPossible(r,c)
                    num_poss = len(possibilities)
                    if(num_poss > 0 and num_poss < least_num_poss):
                        least_num_poss = num_poss
                        best_poss = [r,c]
        return best_poss
    
    def checkFinished(self):
        for r in range(9):
            for c in range(9):
                if(self.F[r][c]==0):
                    return False
        return True
    
    def solve2(self):
        memory = []
        for i in range(81):
            memory.append([])
        stack = []
        best_poss = self.checkBestCase()
        stack.append(best_poss)
        self.num_guesses = 0
        while(not(self.checkFinished())):
            current_pos = peek_stack(stack)
            r = current_pos[0]
            c = current_pos[1]
            if(self.DEBUG == True):
                print("Pos:("+str(r)+","+str(c)+")")
            possibles = self.allPossible(r,c)
            if(len(possibles) == 0):
                temp = stack.pop()
                memory[two2one(r,c)]=[]
                if(self.DEBUG == True):
                    print("Popped:",end='')
                    print(temp)
            else:
                choice = self.choose(possibles,memory[two2one(r,c)])
                self.F[r][c] = choice
                self.num_guesses += 1
                if(self.DEBUG == True):
                    print("Possibles:",end='')
                    print(possibles)
                    print("Memory:",end='')
                    print(memory[two2one(r,c)])
                    print("Choice:" + str(choice))
                memory[two2one(r,c)].append(choice)
                best_poss = self.checkBestCase()
                stack.append(best_poss)
                if(self.DEBUG == True):
                    print("Pushed:",end='')
                    print(best_poss)
            if(self.DEBUG==True):
                self.display()

def two2one(r,c):
    return r*9+c

def one2two(x):
    r = int(x/9)
    x %= 9
    c = x
    return [r,c]
            
def peek_stack(stack):
    if stack:
        return stack[-1]