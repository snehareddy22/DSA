#Check if the Array is Sorted 
#LC LINK:https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

#brute force approach(2 iterations)
def is_sorted(arr):
    n=len(arr)
    for i in range(n):          #check for all numbers in an array
        for j in range(i+1,n):  #check for the next number of i 
            if arr[j]<arr[i]:   #if j<i 
                return False
    return True
arr = [int(x) for x in input().split()]
print(is_sorted(arr))   

# Time Complexity: O(n²) (because of two nested loops)
# Space Complexity: O(1)


#optimal approach(1 iteration)
def is_Sorted(arr, n):
    n=len(arr)
    for i in range(1, n):   # if we check arr[i] < arr[i - 1]  then we get index 0,-1 so we take from 1-n as range
        if arr[i] < arr[i - 1]:
            return False  
    return True                   # return True if no decreasing pair found
arr= [int(x) for x in input().split()]
print(is_Sorted(arr))     

# Time: O(n) → only one pass
# Space: O(1) → no extra space used


#lc code(check sorted and also rotated)
class Solution(object):
    def check(self, nums):
        n=len(nums)
        count=0
#since we’re dealing with rotated arrays, we must also compare the last element with the first element.
#count = 0 → Sorted (Not Rotated)
# count = 1 → sorted + rotated
# count > 1 → Not Sorted or Rotated Properly
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
#The expression (i + 1) % n ensures that when i reaches the last index,
#it wraps around to index 0 (the first element).
                count+=1
        return count<= 1
sol=Solution()
print(sol.check([3,4,5,1,2]))  # True
print(sol.check([2,1,3,4]))    # False
print(sol.check([1,2,3]))      # True
print(sol.check([1,1,1]))      # True

