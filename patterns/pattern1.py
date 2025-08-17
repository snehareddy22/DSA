
# PATTERN 1         
# Input:              
# n = 5                 
# Output:               
# * * * * *               
# * * * * *               
# * * * * *               
# * * * * *
# * * * * *

# Your Task: You don't need to input anything. Complete the function printSquare() which takes  an integer n  
# as the input parameter and print the pattern.
# Time Complexity : O(n2)
# Space Complexity : O(1)

#class Solution:                       for gfg style we should use class as solution
#    def printSquare(self, n):         in python for every class we should take first paramater as self
#        for i in range(n):            outer loop (rows)
#            for j in range(n):         inner loop (columns)
#                print("*", end=" ")    print star and end in used for new line
#            print()                    print in inner loop

def printSqaure(n):
    for i in range(n):
        for j in range(n):
            print("* ",end=" ")
        print()
n=int(input())
printSqaure(n)

