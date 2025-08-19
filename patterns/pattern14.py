# Pattern-14: Increasing Letter Triangle Pattern
# Input Format: N = 6
# Result:   
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F
def printTriangle(N):
    for i in range(N):          # rows: 1..N
        for j in range(i):             # columns: 0..i-1
            ch = chr(ord('A') + j)     # A, B, C, ...
            print(ch, end=" ")
        print()                        # next line
N = int(input())
printTriangle(N)
