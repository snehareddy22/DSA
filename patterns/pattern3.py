#PATTERN 3
# Input Format: N = 6
# Result:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6


def printTriangle(N):
        for i in range(N):
            for j in range(1,i+2):  #because range excludes  
                print(j,end=" ")
            print()
N=int(input())
printTriangle(N)
