#Print 1 to N using recursion
def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)
n=int(input())
func(1,n)
    
#best way
def printNumbers(n):
    if n == 0:              # base case
        return
    printNumbers(n - 1)     # recursive call first
    print(n)                # then print current number
n = int(input("Enter n: "))  # Driver code
printNumbers(n)

#n = 5
# printNumbers(5)
#   printNumbers(4)
#     printNumbers(3)
#       printNumbers(2)
#         printNumbers(1)
#           printNumbers(0) → returns

#TC = O(n)
#SC = O(n)