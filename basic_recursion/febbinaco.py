# #Fibonacci Number
# The first two terms are 0 and 1.
# Every next term is the sum of the previous two terms.
# eg:0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Formula:
# Base case → F(0)=0, F(1)=1
# Formula → F(n) = F(n-1) + F(n-2)
# Example:
# F(2) = F(1) + F(0) = 1 + 0 = 1
# F(3) = F(2) + F(1) = 1 + 1 = 2
# F(4) = F(3) + F(2) = 2 + 1 = 3
# F(5) = F(4) + F(3) = 3 + 2 = 5
# Recursive Fibonacci function
def fibonacci(n):
    # Base cases
    if n == 0:   # F(0) = 0
        return 0
    elif n == 1: # F(1) = 1
        return 1
    # Formula: F(n) = F(n-1) + F(n-2)
    return fibonacci(n-1) + fibonacci(n-2)
# Driver code
N = int(input("Enter the number of terms: "))

print("Fibonacci Series up to", N, "terms:")
for i in range(N+1):   # 0-based indexing
    print(fibonacci(i), end=" ")
