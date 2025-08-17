#PATTERN 4
# Input: 5
# Output:
# 1
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5   

def printTriangle(N):
    for i in range(1,N+1):       #so it start from 1 and end upto n rows
        for j in range(i):        
            print(i,end=" ")    #prints i along the column
        print()
N=int(input())
printTriangle(N)
