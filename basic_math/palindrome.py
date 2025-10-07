#link =https://leetcode.com/problems/palindrome-number/
'''
Check if a number is Palindrome or Not
Problem Statement: Given an integer N, return true if it is a palindrome else return false.
A palindrome is a number that reads the same backward as forward. For example, 121, 1331, 
and 4554 are palindromes because they remain the same when their digits are reversed.
'''
def palindrome(n):
    revNum=0
    dup=n
    while n>0:
        id=n%10
        revNum=(revNum*10)+id
        n=n//10
    print(revNum)
    if dup==revNum:
        print("this is a palindrome")
    else:
        print("this is not palindrome")
n=int(input("enter a number:"))
palindrome(n)


#leetcode
class Solution:
    def isPalindrome(self,x):
        if x<0:     #if a number in negative it cant be palindrome
            return False
        string_x=str(x)  #convert int into str
        rev_string=string_x[::-1]    #reverse the str
        if string_x==rev_string:   #check whether string equal to  reverse str
            return True
        else:
            return False
sol=Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))