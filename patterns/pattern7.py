#PATTERN7
#Input: 5
# Output:
#     *
#    ***  
#   *****
#  *******
# *********


def printTriangle(N):
        for i in range(1, N+1):           # outer loop for rows
            for j in range(N-i):          # inner loop for spaces
                print(" ", end="")
            for j in range(2*i-1):        # inner loop for stars
                 print("*", end="")
            print()   
N=int(input())
printTriangle(N)
