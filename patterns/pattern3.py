#PATTERN 3
# Input Format: N = 6
# Result:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6   rows=1to5  columns=range(1,7)


def printTriangle(N):
        for i in range(1,N+1):    #no of rows= N let N=6(0 to 5)
            for j in range(1,i+1):  #because range excludes so it takes only upto i+1  (1,7)but takes upto 6
                print(j,end=" ")
            print()
N=int(input())
printTriangle(N)
