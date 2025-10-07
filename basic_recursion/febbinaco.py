#Fabonacci Number
#LC LINK=https://leetcode.com/problems/fibonacci-number/submissions/1793420575/
#The Fibonacci sequence is a series of numbers where each number is the sum of the 
# two preceding ones.eg :0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacci(n):
    if n == 0:    # Base cases
        return 0
    elif n == 1: 
        return 1
    return fibonacci(n-1) + fibonacci(n-2)    # Formula: F(n) = F(n-1) + F(n-2)
n = int(input("Enter the number of terms: "))
print(fibonacci(n))  
#TC=O(2ⁿ)
#SC=O(n)


#Optimized Recursive Fibonacci with Memoization
def fibonacci(n, memo={}):
    if n in memo:  # If we already calculated fibonacci(n), return it
        return memo[n]
    if n == 0:     # Base case: F(0) = 0
        memo[0] = 0
        return 0
    if n == 1:     # Base case: F(1) = 1
        memo[1] = 1
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
n = int(input("Enter n: "))
print(f"Fibonacci({n}) =", fibonacci(n))

#TC=O(n)
#SC=O(n)



#iterative way
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    prev, curr = 0, 1   # F(0) and F(1)
    for i in range(2, n + 1):
        next_num = prev + curr   # F(i) = F(i-1) + F(i-2)
        prev, curr = curr, next_num  # Update previous two numbers
    return curr
n = int(input("Enter n: "))
print(f"Fibonacci({n}) =", fibonacci(n))
#TC=O(n)
#SC=O(1)


