#Pattern - 9: Diamond Star Pattern
# Input Format: N = 6
# Result:   
#      *
#     ***
#    ***** 
#   *******
#  *********
# ***********  
# ***********
#  *********
#   *******
#    ***** 
#     ***    
#      *
def printTriangle(N):
        for i in range(1, N+1):           # outer loop for rows
            for j in range(N-i):          # inner loop for spaces
                print(" ", end="")
            for j in range(2*i-1):        # inner loop for stars
                 print("*", end="")
            print()   
        for i in range(N,0,-1):
        # print spaces
            for j in range(N - i):
                print(" ", end="")
        # print stars
            for j in range(2*i- 1):
                print("*",end="")
            print()  # new line after each row
N=int(input())
printTriangle(N)