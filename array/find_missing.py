#Find the missing number in an array
#LC LINK:https://leetcode.com/problems/missing-number/

#Brute Force Approach: (Using Linear Search / Nested Loops)
def check_missing(arr):
    n=len(arr)
    for i in range(1,n+2):
        if i not in  arr:
            print(i)
            break
arr=list(map(int,input().split()))
print(check_missing(arr))
# Time Complexity: O(n²)
# Space Complexity: O(1)

#Better Approach (Using Hashing / Frequency Array)
def find_missing(arr):
    n = len(arr)
    hash_arr = [False] * (n + 2)   # numbers from 1 to n+1
    # Mark all present numbers
    for num in arr:
        if num <= n + 1:          # ensure within expected range
            hash_arr[num] = True
    # Find the number which is still False
    for i in range(1, n + 2):
        if not hash_arr[i]:
            return i
arr =list(map(int,input().split()))
print(find_missing(arr)) 
# Time: O(n)
# Space: O(n)


# Optimal Approach (Using Formula)
def find_missing(arr):
    n = len(arr)
    actualsum=sum(arr)
    originalsum=(n+1)*(n+2)//2
    return originalsum-actualsum
arr =list(map(int,input().split()))
print(find_missing(arr))
# Time: O(n)
# Space: O(1)

#Optimal Approach (Using XOR)
#  a ⊕ a = 0
#  a ⊕ 0 = a
def find_missing(arr):
    n = len(arr)
    xor1 = 0   #initialize
    xor2 = 0
    # XOR1 of all numbers from 1 to n+1
    for i in range(1, n + 2):
        xor1 ^= i
    # XOR2 of all elements in the array
    for num in arr:
        xor2 ^= num
    # Missing number
    return xor1 ^ xor2
arr = list(map(int, input().split()))
print(find_missing(arr))
# Time: O(n)
# Space: O(1)


#LC 
class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        xor1=0
        xor2=0
        for i in range(0,n+1):
            xor1^=i
        for j in nums:
            xor2^=j
        return xor1^xor2
Sol=Solution()
print(Sol.missingNumber([3,0,1]))
print(Sol.missingNumber([0,1]))    
print(Sol.missingNumber([9,6,4,2,3,5,7,0,1]))  