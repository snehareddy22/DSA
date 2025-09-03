#Remove Duplicates in-place from Sorted Array
''''
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in 
place such that each unique element appears only once. The relative order of the elements should be kept the same.
If there are k elements after removing the duplicates, then the first k elements of the array should 
hold the final result. It does not matter what you leave beyond the first k elements.
Note: Return k after placing the final result in the first k slots of the array.

Brute Force with Set
Declare a set → because sets store only unique elements.
Traverse the array and insert each element into the set.
This automatically removes duplicates.
Copy the elements of the set back into the array from the beginning.
Return the size of the set.
'''
from typing import List
def removeDuplicates(arr: List[int]) -> int:
    st = set(arr)   #put all elements into a set (removes duplicates)
    unique = sorted(st)  #convert set back to a sorted list
    for i in range(len(unique)):   #copy unique elements back into arr
        arr[i] = unique[i]   #return number of unique elements
    return len(unique)

arr = [1, 1, 2, 2, 2, 3, 3]
k = removeDuplicates(arr)
print("The array after removing duplicate elements is:")
for i in range(k):
     print(arr[i], end=" ")

#tc=nlogn+n
#sc=o(n)
'''
#optimized solution using two pointer
Two pointers
Intuition: We can think of using two pointers ‘i’ and ‘j’, we move ‘j’ till we don't get a number arr[j] which 
is different from arr[i]. As we got a unique number we will increase the i pointer and update its value by arr[j]. 
Approach:
Take a variable i as 0;
Use a for loop by using a variable ‘j’ from 1 to length of the array.
If arr[j] != arr[i], increase ‘i’ and update arr[i] == arr[j].
 After completion of the loop return i+1, i.e size of the array of unique elements.
 '''
from typing import List
def remove_dup(arr: List[int]) -> int:
    n = len(arr)
    if n == 0:   # handle empty array
        return 0
    i = 0   # slow pointer
    for j in range(1, n):   # fast pointer
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1   # length of unique elements
arr = [1, 2, 3, 3, 4, 4, 5, 5, 5]
R = remove_dup(arr)
print("The array after removing duplicates is:")
for s in range(R):
    print(arr[s], end=" ")



#leetcode
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
sol = Solution()
nums1 = [1, 1, 2]
k1 = sol.removeDuplicates(nums1)
print("Example 1:")
print("k =", k1)
print("Unique elements:", nums1[:k1])
print()

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = sol.removeDuplicates(nums2)
print("Example 2:")
print("k =", k2)
print("Unique elements:", nums2[:k2])

#TC = O(n)
#SC = O(1).