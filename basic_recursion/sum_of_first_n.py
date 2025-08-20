#Sum of first N numbers
#parametres way
def param_sum(i, s):
    if i < 1:          # base case
        print(s)       # final result
        return
    param_sum(i - 1, s + i)   # recursive call with updated i and sum
# Driver code
n = int(input("Enter n: "))
param_sum(n, 0)          #start from here

#functioanl way
def func(n):
    # base case
    if n == 0:
        return 0
    
    # recursive case
    return n + func(n - 1)

# driver code
n = int(input("Enter n: "))
print("Sum of first", n, "natural numbers is:", func(n))


 
# Call stack:
# func(4) = 4 + func(3)
# func(3) = 3 + func(2)
# func(2) = 2 + func(1)
# func(1) = 1 + func(0)
# func(0) = 0

# Now the recursion resolves back:
# func(1) = 1 + 0 = 1
# func(2) = 2 + 1 = 3
# func(3) = 3 + 3 = 6
# func(4) = 4 + 6 = 10