#Count Subarray sum Equals K

#brute force
def subarraySum(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    return count
# Example:
nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k)) 

#better appraoch
def subarraySum(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if prefix[j] - prefix[i] == k:
                count += 1
    return count
# Example:
nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))   

#optimal approach
from collections import defaultdict
def countSubarraysWithSumK(arr, k):
    # To store frequency of each prefix sum
    prefix_count = defaultdict(int)
    # prefix_sum = sum of all elements up to current index
    prefix_sum = 0
    # Count of subarrays whose sum == k
    count = 0
    # Very important: there's one way to have sum=0 before starting
    prefix_count[0] = 1
    # Traverse the array
    for num in arr:
        prefix_sum += num   # update running sum
        # Find how many times (prefix_sum - k) occurred before
        # Because that means a subarray ending here has sum = k
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]
        # Record current prefix_sum
        prefix_count[prefix_sum] += 1
    return count
# Example:
arr = [3, 1, 2, 4]
k = 6
print("Number of subarrays with sum = k:", countSubarraysWithSumK(arr, k))


