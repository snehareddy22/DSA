#Two Sum : Check if a pair with given sum exists in Array
#brute force(using loops)
def two_sum(arr, target):
    n = len(arr)
    for i in range(n):                   # pick first number
        for j in range(i + 1, n):        # pick next number after i
            if arr[i] + arr[j] == target:  # check if their sum matches target
                return True               # found the pair
    return False                          # no pair found
arr = list(map(int, input().split()))
target = int(input())
print(two_sum(arr, target))
#TC=O(n2)
#SC=O(1)


#optimal approach(hashmap)
def two_sum(arr, target):
    seen = {}               # store {number: index}
    for i, num in enumerate(arr):
        rem = target - num  # number we need
        if rem in seen:     # if we’ve seen the needed number
            return True     # pair found
        seen[num] = i       # store current number with its index 
    return False            # no pair found
arr = list(map(int, input().split()))
target = int(input())
print(two_sum(arr, target))

#for prinitng num
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [seen[rem], i]   
            seen[num] = i
        return None
#TC=O(n)
#sc=o(n)


#optimal approach(Two pointers)
def two_sum(arr, target):
    arr.sort()  # make sure array is sorted
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right] 
        if curr_sum == target:
            return True  # found the pair
        elif curr_sum < target:
            left += 1    # need bigger sum
        else:
            right -= 1   # need smaller sum
    return False
arr = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target sum: "))
print(two_sum(arr, target))
#TC=o(nlogn)
#sc=o(1)