#PATTERN 8
# Input Format: N = 6
# Result:     
# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *

def printTriangle(N):
    for i in range(1, N + 1):
        # print spaces
        for j in range(i - 1):
            print(" ", end="")
        # print stars
        for j in range(2*(N - i) + 1):
            print("*", end="")
        print()  # new line after each row
N=int(input())
printTriangle(N)
