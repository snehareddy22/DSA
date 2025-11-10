#Longest Consecutive Sequence
#brute force(check every possible sequence manually)
def longest_consecutive(arr):
    n = len(arr)
    if n == 0:
        return
    max_len = 0  # to store the longest sequence length
    for num in arr:
        curr = num
        length = 1
        while (curr + 1) in arr:  # check for next consecutive numbers
            curr += 1
            length += 1
        max_len = max(max_len, length)    # update max length
    return max_len
arr = list(map(int, input().split()))
print(longest_consecutive(arr))
#TC=O(n²)
#SC=O(1)



#better apprach using sorting
def longest_consecutive(arr):
    n = len(arr)
    if n == 0:
        return 0
    arr.sort()  # sort the array first
    max_len = 1
    curr_len = 1
    for i in range(1, n):
        if arr[i] == arr[i - 1]:    # skip duplicates
            continue
        if arr[i] == arr[i - 1] + 1:   # consecutive
            curr_len += 1
        else:
            curr_len = 1                # reset if not consecutive
        max_len = max(max_len, curr_len)
    return max_len
arr = list(map(int, input().split()))
print(longest_consecutive(arr))
#TC=O(n log n)
#SC=O(1)


#optimal approach(using hash sets)
class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)             # store all elements for O(1) lookup
        longest = 0
        for n in numSet:
            if (n - 1) not in numSet:   # check if 'n' is the start of a sequence
                length = 1
                while (n + length) in numSet:   
                    length += 1
                longest = max(longest, length)
        return longest

arr = list(map(int, input().split()))
print(longest_consecutive(arr))
#TC=O(n)
#SC=O(n)




                
