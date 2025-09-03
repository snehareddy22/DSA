#Check if an Array is Sorted
#Problem Statement: Given an array of size n, write a program to check if the given array is sorted
#  in  order or not. If the array is sorted then return True, Else return False.
'''
We will start with the element at the 0th index, and will compare it with all of its future elements
that are present in the array.If the picked element is smaller than or equal to all of its future values 
then we will move to the next Index/element until the whole array is traversed.if any of the picked elements
is greater than its future elements, Then simply we will return False.If the size of the array is Zero or 
One i.e ( N = 0 or N = 1 ) or the entire array is traversed successfully then we will simply return True.
'''
def is_sorted(arr,n):
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True
arr=[1,3,2,5,6]
n=len(arr)
is_sorted(arr,n)

# O(n) time (one pass through the array)
# O(1) space (only a few variables)


#leetcode 
class Solution(object):
    def check(self, nums):
        n=len(nums)
        count=0
#since we’re dealing with rotated arrays, we must also compare the last element with the first element.
#count = 0 → already sorted
# count = 1 → sorted + rotated
# count ≥ 2 → not possible
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                count+=1
        return count<= 1
sol=Solution()
print(sol.check([3,4,5,1,2]))  # True
print(sol.check([2,1,3,4]))    # False
print(sol.check([1,2,3]))      # True
print(sol.check([1,1,1]))      # True
    