#Print N to 1 using Recursion
def printNumbersReverse(n):
    if n == 0:    #base case
        return
    print(n)                 # print current first
    printNumbersReverse(n - 1) # then go smaller upto base case n==0 and stops
n=int(input())
printNumbersReverse(n)


def func(i):
    if i < 1:         # base case: stop when i < 1
        return
    print(i)          # print current
    func(i - 1)       # move downwards

# Driver code
n = int(input("Enter n: "))
func(n)

#TC = O(n)
#sC = O(n)