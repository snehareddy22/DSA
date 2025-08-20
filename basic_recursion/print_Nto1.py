#Print N to 1 using Recursion
def printNumbersReverse(n):
    if n == 0:
        return
    print(n)                 # print current first
    printNumbersReverse(n - 1)  # then go smaller


def func(i,n):
    if i>n:
        return
    func(i+1,n)
    print(i)
n=int(input())
func(1,n)

def func(i):
    if i < 1:         # base case: stop when i < 1
        return
    print(i)          # print current
    func(i - 1)       # move downwards

# Driver code
n = int(input("Enter n: "))
func(n)

    