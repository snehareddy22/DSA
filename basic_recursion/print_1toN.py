#Print name N times using recursion
def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)
n=int(input())
func(1,n)
    

def printNumbers(n):
    # base case
    if n == 0:
        return
    # recursive call first
    printNumbers(n - 1)
    # then print current number
    print(n)
# Driver code
n = int(input("Enter n: "))
printNumbers(n)
