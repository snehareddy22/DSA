# #Check if the given String is Palindrome or not
# Problem Statement: "Given a string, check if the string is palindrome or not."  A string is 
# said to be palindrome if the reverse of the string is the same as the string.
# Example 1:
# Input: Str =  “ABCDCBA”
# Output: Palindrome
# Explanation: String when reversed is the same as string.
# Example 2:
# Input: Str = “TAKE U FORWARD”
# Output: Not Palindrome
# Explanation: String when reversed is not the same as string.


def isPalindromeRecursive(s, left, right):
    # Base Case 1: If left >= right, all chars matched → palindrome
    if left >= right:
        return True
    
    # Base Case 2: If characters don't match → not a palindrome
    if s[left] != s[right]:
        return False
    
    # Recursive step: move inward
    return isPalindromeRecursive(s, left + 1, right - 1)

s1 = "ABCDCBA"
s2 = "TAKE U FORWARD"

print(f"{s1}: {'Palindrome' if isPalindromeRecursive(s1, 0, len(s1) - 1) else 'Not Palindrome'}")
print(f"{s2}: {'Palindrome' if isPalindromeRecursive(s2, 0, len(s2) - 1) else 'Not Palindrome'}")

# Input: "ABCDCBA"
# Step 1: Compare A == A
# Step 2: Compare B == B
# Step 3: Compare C == C
# Step 4: Compare D == D (center reached)
# ✅ Palindrome

# Input: "TAKE U FORWARD"
# Step 1: Compare T != D → ❌ Not Palindrome

# Function to check if a string is a palindrome
def isPalindrome(s):
    # Initialize two pointers: one at the start, one at the end
    left = 0
    right = len(s) - 1

    # Loop until the two pointers meet
    while left < right:
        # Skip left character if it is not alphanumeric (ignores spaces, punctuation)
        if not s[left].isalnum():
            left += 1
        # Skip right character if it is not alphanumeric
        elif not s[right].isalnum():
            right -= 1
        # If characters at left and right don't match (case insensitive), not a palindrome
        elif s[left].lower() != s[right].lower():
            return False
        else:
            # If they match, move both pointers closer
            left += 1
            right -= 1

    # If loop completes, it's a palindrome
    return True


# Main block to test the function
# Input string
s = "ABCDCBA"   # Change this value to test other strings
# Function call
ans = isPalindrome(s)
# Output
if ans:
    print("Palindrome")
else:
    print("Not Palindrome")
