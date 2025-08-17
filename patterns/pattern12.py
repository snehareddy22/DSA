# Pattern - 12: Number Crown Pattern
# Input Format: N = 6
# Result:   
# 1          1
# 12        21
# 12       321
# 1234    4321
# 12345  54321
# 123456654321
def printTriangle(N):
    for i in range(1, N+1):
        # left side numbers
        for j in range(1, i+1):
            print(j, end="")
        # spaces
        for j in range(2*(N-i)):
            print(" ", end="")
        # right side numbers
        for j in range(i, 0, -1):
            print(j, end="")
        print()  # new line after each row
N = int(input())
printTriangle(N)
