#Sum of first N numbers

#parametres way
def para_sum(i, s):  
    if i < 1:          # base case
        print(s)       # final result
        return
    para_sum(i - 1, s + i)   # recursive call with updated i and sum
# Driver code
n = int(input("Enter n: "))
para_sum(n, 0)          #start from here
#eg n=5
# para_sum(5, 0) → para_sum(4, 5)
# para_sum(4, 5) → para_sum(3, 9)
# para_sum(3, 9) → para_sum(2, 12)
# para_sum(2, 12) → para_sum(1, 14)
# para_sum(1, 14) → para_sum(0, 15)
# para_sum(0, 15) → base case → print(15)


#functioanl way
def func(n):
    if n == 0:   # base case
        return 0
    return n + func(n - 1)   # recursive case
n = int(input("Enter n: "))
print("Sum of first", n, "natural numbers is:", func(n))

# func(5) = 5 + func(4)
# func(4) = 4 + func(3)
# func(3) = 3 + func(2)
# func(2) = 2 + func(1)
# func(1) = 1 + func(0)
# func(0) = 0  # base case

#TC=O(n)
#SC=O(n)