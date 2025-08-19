#Reverse a number
#leetcode link:https://leetcode.com/problems/reverse-integer/
#You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
# Input: n = 25
# Output: 52
# Explanation: Reverse of 25 is 52.


n = int(input("Enter an integer: "))
revNum = 0   # Initialize a variable 'revNum' to store the reverse of the input integer.
while n > 0:  # Extract the last digit of 'n' and store it in 'ld'.
    ld = n % 10    #takes the last digit
    revNum = (revNum * 10) + ld     # Multiply the current reverse number by 10 and add the last digit.
    n = n // 10      #Remove the last digit from 'n' adn again continue loop
print(revNum)


# by using slicing
n = input("Enter a number: ")
reversed_n = n[::-1] 
print(reversed_n)


#leetcode question
class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1         # remember the sign
        x_str = str(abs(x))                # convert to string
        reversed_str = x_str[::-1]         # reverse string
        reversed_num = sign * int(reversed_str)  # convert back to int with sign
        
        # Check 32-bit overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num

#check examples
sol = Solution()
print(sol.reverse(123))    # Output: 321
print(sol.reverse(-123))   # Output: -321
print(sol.reverse(120))    # Output: 21
print(sol.reverse(1534236469))  # Output: 0 (overflow)
