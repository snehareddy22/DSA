#PATTERN 6
# Input: 5
# Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2  
# 1 


def printTriangle(self, N):
    for i in range(N, 0, -1):       # start from N down to 1
        for j in range(1, i+1):     # print numbers from 1 to i
            print(j, end=" ")
        print()
N=int(input())
printTriangle(N)
