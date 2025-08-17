
#PATTERN 2
# Input:
# n = 5
# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# Your Task:
# You don't need to input anything. Complete the function printTriangle() which takes an integer n  
# as the input parameter and prints the pattern accordingly.
# Expected Time Complexity : O(n2)
# Expected Auxilary Space : O(1)
def printTriangle(N):
    for i in range(1,N+1):  #CALCULATE NO OF ROWS 0,1,2,3
        for j in range(i):   #NO OF COLUMNS MUST BE 1 MORE THAN ROWS 1,2,3,4
            print("* ",end=" ")
        print()
N=int(input())
printTriangle(N)
