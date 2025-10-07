#Factorial of a Number Recursive
def factorial_recursive(n):
    if n == 0 or n == 1:    # base case
        return 1 
    return n * factorial_recursive(n - 1)   # recursive case
n = int(input("Enter a number: "))
print("Factorial (Recursive) of", n, "is:", factorial_recursive(n))

# Recursive:
# fact(5) = 5 * fact(4)
# fact(4) = 4 * fact(3)
# fact(3) = 3 * fact(2)
# fact(2) = 2 * fact(1)
# fact(1) = 1  ← base

# Resolving back:
# 1 → 2 → 6 → 24 → 120


#Iterative Way (using a loop)
def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
n = int(input("Enter a number: "))
print("Factorial (Iterative) of", n, "is:", factorial_iterative(n))
#eg n=5
# fact = 1
# 1*1 = 1
# 1*2 = 2
# 2*3 = 6
# 6*4 = 24
# 24*5 = 120
