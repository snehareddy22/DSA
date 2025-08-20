#Factorial of a Number : Iterative and Recursive
def factorial_recursive(x):
    # base case
    if x == 0 or x == 1:
        return 1
    
    # recursive case
    return x * factorial_recursive(x - 1)

# Driver code
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
def factorial_iterative(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

# Driver code
n = int(input("Enter a number: "))
print("Factorial (Iterative) of", n, "is:", factorial_iterative(n))

# fact = 1
# 1*1 = 1
# 1*2 = 2
# 2*3 = 6
# 6*4 = 24
# 24*5 = 120
