#               count all Digits of a Number
# You are given an integer n. You need to return the number of digits in the number.
# The number will have no leading zeroes, except when the number is 0 itself.
# Input: n = 14
# Output: 2
# Explanation: There are 2 digits in 14.

def countDigits(n):   # Function to count the number of digits in an integer 'n'.
    cnt = 0    # Initialize a counter variable 'cnt' to store the count of digits.
    while n > 0:  # While loop iterates until 'n'becomes 0 (no more digits left).
        cnt = cnt + 1    # Increment the counter for each digit encountered.
        n = n // 10 #Return the count of digits.   
    return cnt
n=int(input("Enter a numner:"))
print(countDigits(n))



#using len()
def count_digits(n):
    # Convert the number to string and return its length
    return len(str(n))
n = int(input("Enter a number: "))
print(count_digits(n))
