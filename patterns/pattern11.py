#Pattern - 11: Binary Number Triangle Pattern
# Input Format: N = 6
# Result:   
# 1
# 01
# 101
# 0101
# 10101
# 010101
def printTriangle(N):
    for i in range(1, N+1):          # loop for rows
        start = 1 if i % 2 != 0 else 0   # odd row → start with 1, even row → start with 0
        for j in range(i):            # columns (no of didgits to print)
            print(start, end="")
            start = 1 - start         # flip between 1 and 0
        print()                       # move to next line

# Input
N = int(input())
printTriangle(N)
