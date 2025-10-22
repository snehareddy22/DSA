#Remove Duplicates in-place from Sorted Array
#LC LINK:https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1795834462/

#naive sol
def remove_dup(arr,n):
    temp=[0]*n           #create a new list as temp
    temp[0]=arr[0]       #as first element is laways unique
    res=1                #initialize res
    for i in range(1,n): #0th element is already placed in temp
        if temp[res-1]!=arr[i]:  #check for arr elemnt and temp before elemnt  if not equal
            temp[res]=arr[i]     #add the elment to temp list
            res+=1               #increase the res count
    for i in range(0,res):        #add all the elemnts of res into the arr
        arr[i]=temp[i]
    return res                    #return the res

# Time: O(n) (two passes: one to find uniques, one to copy back)
# Space: O(n) (uses extra temp array)


#optmimal approach(two pointers)
def remove_dup(arr,n):
    if n==0:         #edge case
        return 0
    res=1             #first elemnt is always unique
    for i in range(1,n):  #for evry emelrnt check is the last added res is equal or not
        if arr[res-1]!=arr[i]:    
            arr[res]=arr[i]    #if not add it
            res+=1             #increase count to 1
    return res
arr= [int(x) for x in input().split()]
n=len(arr)
print(remove_dup(arr,n))

# Time: O(n)
# Space: O(1) (true in-place, no extra array)


#lc code
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        res=1
        for i in range(1,len(nums)):
            if nums[res-1]!=nums[i]:
                nums[res]=nums[i]
                res+=1
        return res
sol=Solution()
nums1= [1,1,2]
k1=sol.removeDuplicates(nums1)
print("nums",nums1[:k1])
print()
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = sol.removeDuplicates(nums2)
print("nums", nums2[:k2])
