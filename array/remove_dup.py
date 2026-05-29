#Remove Duplicates in-place from Sorted Array
#LC LINK:https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1795834462/

#naive sol
def remove_dup(arr):
    seen=set()
    seen.update(arr)
    return list(seen)
arr=list(map(int,input().split()))
print(remove_dup(arr))
# Time: O(n)
# Space: O(n) 




#optmimal approach(two pointers)
# i → scanning pointer (goes through every element)
# res → slow pointer / position of next unique element
# They move at different speeds, that’s why it’s called two-pointer technique.
def remove_dup(arr,n):
    if n==0:         #edge case
        return 0
    res=1             #first elemnt is always unique
    for i in range(1,n):  #for evry element check is the last added res is equal or not
        if arr[res-1]!=arr[i]:    
            arr[res]=arr[i]    #if not add it
            res+=1             #increase count to 1
    return res
arr= [int(x) for x in input().split()]
n=len(arr)
print(remove_dup(arr,n))

#DRY RUN
'''
arr = [10, 10, 20, 20, 20, 30, 30]
initialize res = 1 and i = 1
| i | arr[i] | arr[res-1] | Action           | Array after step             | res |
| - | ------ | ---------- | ---------------- | ---------------------------- | --- |
| 1 | 10     | 10         | same → skip      | [10, 10, 20, 20, 20, 30, 30] | 1   |
| 2 | 20     | 10         | different → copy | [10, 20, 20, 20, 20, 30, 30] | 2   |
| 3 | 20     | 20         | same → skip      | unchanged                    | 2   |
| 4 | 20     | 20         | same → skip      | unchanged                    | 2   |
| 5 | 30     | 20         | different → copy | [10, 20, 30, 20, 20, 30, 30] | 3   |
| 6 | 30     | 30         | same → skip      | unchanged                    | 3   |
Unique elements count = 3
First 3 elements = [10, 20, 30]

| unique zone | garbage zone |
| 0 ... res-1 | res ... n-1 |

Time: O(n)
Space: O(1) (true in-place, no extra array)
'''


