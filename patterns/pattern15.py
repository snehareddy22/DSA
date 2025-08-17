# Pattern-15: Reverse Letter Triangle Pattern
# Input Format: N = 6
# Result:   
# A B C D E F
# A B C D E 
# A B C D
# A B C
# A B
# A
def printTriangle(N):
    for i in range(N, 0, -1):          # rows: N down to 1
        for j in range(i):             # columns: 0..i-1
            ch = chr(ord('A') + j)     # A, B, C, ...
            print(ch, end=" ")
        print()                        # next line
N = int(input())
printTriangle(N)
