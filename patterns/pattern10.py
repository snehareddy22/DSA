#Pattern - 10: Half Diamond Star Pattern
#Input Format: N = 6
# Result:   
#      *
#      **
#      *** 
#      ****
#      *****
#      ******  
#      *****
#      ****
#      ***    
#      **
#      *
def printTriangle(N):
    # 1st Half (increasing triangle)
    for i in range(N):       # loop from 1 → N
        for j in range(i):        # print i stars
            print("*", end="")
        print()                   # new line
    
    # 2nd Half (decreasing triangle)
    for i in range(N, 0, -1):   # loop from N-1 → 1
        for j in range(i):        # print i stars
            print("*", end="")
        print()                   # new line

# Input
N = int(input())
printTriangle(N)
