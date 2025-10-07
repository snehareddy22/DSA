#Check if the given String is Palindrome or not
#LC LINK= https://leetcode.com/problems/valid-palindrome/submissions/1793394356/

#two pointers method
def isPalindromeRecursive(s, start, end):
    if start >= end:
        return True
    return (s[start] == s[end]) and isPalindromeRecursive(s, start + 1, end - 1)
print(isPalindromeRecursive("madam", 0, 4))  

#eg
# Call: start=0, end=4
# Match: m == m ✅ → recurse
# Call: start=1, end=3
# Match: a == a ✅ → recurse
# Call: start=2, end=2
# Base case reached ✅
# Result: True

#tc=o(n)
#sc=o(n)

#Functional Recursion
def is_palindrome(s):
    if len(s) <= 1:   # base case: empty or single char
        return True
    if s[0] != s[-1]:  # mismatch
        return False
    return is_palindrome(s[1:-1])  # recurse on substring
print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False

# "madam" → compares 'm' and 'm', then recurses on "ada".
# "ada" → compares 'a' and 'a', then recurses on "d".
# "d" → length ≤ 1 → base case → return True.
# "madam" is palindrome.
# "hello" → compares 'h' and 'o' → mismatch → return False.

#tc=o(n)
#sc=o(n)



#LC question
class Solution:
    def isPalindrome(self, s):   
        s = s.lower()                   #Convert the string to lowercase
        left, right = 0, len(s) - 1     #Initialize two pointers: start and end of the string
        while left < right:
            while left < right and not s[left].isalnum(): #Skip non-alphanumeric chars from the left
                left += 1
            while left < right and not s[right].isalnum(): #Skip non-alphanumeric chars from the right
                right -= 1
            if s[left] != s[right]:    # Compare characters at left and right pointers
                return False
            left += 1                  # Move pointers inward
            right -= 1
        return True
# Test locally
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))                      # False
print(sol.isPalindrome(" "))                               # True

#TC O(n)	
#SC O(1)	