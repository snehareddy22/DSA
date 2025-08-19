#Divisors of a Number
# You are given an integer n. You need to find all the divisors of n. Return all the divisors of n
# as an array or list in a sorted order.
# Input: n = 6
# Output = [1, 2, 3, 6]
# Explanation: The divisors of 6 are 1, 2, 3, 6.

n = int(input("Enter a number: "))
divisors = []       # Initialize an empty list to store divisors
for i in range(1, n + 1):   # Loop from 1 to n and check divisibility
    if n % i == 0:
        divisors.append(i)  # add i to list if it divides n
print("Divisors of", n, "are:", divisors)  # Print the sorted list of divisors
