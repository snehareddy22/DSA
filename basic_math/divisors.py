'''
Divisors of a Number
You are given an integer n. You need to find all the divisors of n. Return all the divisors of n
as an array or list in a sorted order.
Input: n = 6
Output = [1, 2, 3, 6]
Explanation: The divisors of 6 are 1, 2, 3, 6.
'''
#brute force
n = int(input("Enter a number: "))
divisors = []               # Initialize an empty list to store divisors
for i in range(1, n + 1):   # Loop from 1 to n and check divisibility
    if n % i == 0:          #find divisors
        divisors.append(i)  # add i to list if it divides n
print("Divisors of", n, "are:", divisors)  # Print the sorted list of divisors
#TC = O(n) Loop runs from 1 to n → n iterations
#SC = O(n)  Extra space: divisors list stores all divisors

#optimal approach to give unsorted divisors list
def print_divisors(n):
    i=1
    while(i*i<=n):       #ensures you only check divisors up to the square root of n
        if (n%i==0):
            print(i)
            if (i!=n/i):
                print(n/i)
        i+=1
n=int(input())
print_divisors(n)
#TC = O(√n)
#SC = O(1)


#optimal solution for getting sorted divisors
def print_divisors(n):
    i = 1
    while i * i <= n:         # Loop 1: smaller divisors
        if n % i == 0:
            print(i)
        i += 1
    i -= 1                     # Start from last i used in first loop
    while i >= 1:              # Loop 2: paired divisors
        if n % i == 0 and i != n // i:  # avoid duplicates for perfect squares
            print(n // i)
        i -= 1
#TC = O(√n)
#SC = O(1)
