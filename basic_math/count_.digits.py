'''count all Digits of a Number
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.
Input: n = 14
Output: 2
# Explanation: There are 2 digits in 14.
'''
#using loops
def countDigits(n):      # Function to count the number of digits in an integer 'n'.
    cnt = 0              # Initialize a counter variable 'cnt' to store the count of digits.
    while n > 0:         # While loop iterates until 'n'becomes 0 (no more digits left).
        cnt = cnt + 1    # Increment the counter for each digit encountered.
        n = n // 10      #Return the count of digits.   
    return cnt
n=int(input("Enter a numner:"))
print(countDigits(n))
#TC=log₁₀(n)
#because dividing n by 10 each time reduces its size exponentially,
# so the loop runs roughly log₁₀(n) times instead of n times.
#SC=o(1)  (constant space)


#using len()
def count_digits(n):
    return len(str(n))  # Convert the number to string and return its length
n = int(input("Enter a number: "))
print(count_digits(n))
#TC=log₁₀(n)
#becouse str(n) converts the integer n to a string.
#SC=O(log₁₀ n) creates a new string

#using recursion
def count_digits(n):
    n = abs(n)
    if n<10:
        return 1
    return 1 + count_digits(n // 10)
print(count_digits(12345))
#TC=log₁₀(n) Each recursive call reduces n by a factor of 10 → roughly log₁₀ n calls.
#SC=log₁₀(n) Recursion stack stores roughly log₁₀ n calls → O(log₁₀ n) space.

#by importing math(most optimal)
import math
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1 
print(count_digits(12345))  # Output: 5
#TC=O(1)
#SC=O(1)