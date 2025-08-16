
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
def printTriangle(N):           #define function
        for i in range(N):       #outer loop for no of rows
            for j in range(i+1):  #inner loop for evry low n,n+1 stars should print
                print("* ",end=" ")
            print()
N=int(input())
printTriangle(N)
