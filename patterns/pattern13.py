# Pattern - 13: Increasing Number Triangle Pattern
# Input Format: N = 6
# Result:   
# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11  12  13  14  15
# 16  17  18  19  20  21
def printTriangle(N):
    num = 1   # starting number
    for i in range(1, N+1):        # rows
        for j in range(i):    # columns
            print(num, end=" ")
            num += 1
        print()   # new line after each row
N = int(input())
printTriangle(N)
