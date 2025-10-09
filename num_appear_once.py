#Find the number that appears once, and the other numbers twice
#LC CODE:https://leetcode.com/problems/single-number/submissions/1795843057/
#naive approach
def find_single(arr, n):
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]
    return -1  # if nothing found
arr= [int(x) for x in input().split()]
n=len(arr)
print(find_single(arr,n))
# Total c: O(n²) 
# Space c: O(1)

#optimal apprach
# Properties of XOR (^ in Python):
# a ^ a = 0 → XOR of a number with itself is 0
# a ^ 0 = a → XOR of a number with 0 is the number itself
# XOR is commutative and associative, order doesn’t matter
def find_single_xor(arr):
    result = 0
    for num in arr:
        result ^= num  # XOR with each element
    return result
arr= [int(x) for x in input().split()]
print(find_single_xor(arr,n))

# Time: O(n) → single pass
# Space: O(1) → constant extra space

#lc 
class Solution(object):
    def singleNumber(self, nums):
        result=0
        for i in nums:  #range(nums) expects an integer, but nums is a list.
            result^=i
        return result
sol=Solution()
nums = [2, 2, 1]
print(sol.singleNumber(nums))  # Output: 1
nums = [4, 1, 2, 1, 2]
print(sol.singleNumber(nums))  # Output: 4
nums = [1]
print(sol.singleNumber(nums))  # Output: 1






