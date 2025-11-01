# Longest Subarray with Sum K (naive)
def is_subsum(arr, K):
    n = len(arr)
    lenght=0
    for i in range(n):            # start index of subarray
        curr_sum = 0              # current sum
        for j in range(i, n):     # end index of subarray
            curr_sum += arr[j]    # add current element
            if curr_sum == K:     # check if sum equals K
                lenght=max(lenght,j-i+1)
    return lenght
arr = [int(x) for x in input("Enter array: ").split()]
K = int(input("Enter sum K: "))
print(is_subsum(arr, K))

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Longest Subarray with Sum K (optimal)
def longest_subarray_sum_k(arr, k):
    prefix_sum = 0                 # running total
    seen = {}                      # stores first index of each prefix_sum
    max_len = 0                    # longest length found so far
    for i in range(len(arr)):
        prefix_sum += arr[i]       # keep adding elements one by one
        # Case 1: subarray from 0..i has sum == k
        if prefix_sum == k:
            max_len = i + 1
        # Case 2: check if (prefix_sum - k) was seen before
        if (prefix_sum - k) in seen:
            length = i - seen[prefix_sum - k]   # subarray between those indices has sum k
            max_len = max(max_len, length)
        # Case 3: store the first time we see a prefix_sum
        if prefix_sum not in seen:
            seen[prefix_sum] = i
    return max_len
arr = [int(x) for x in input("Enter array: ").split()]
K = int(input("Enter sum K: "))
print(is_subsum(arr, K))

# Time Complexity: O(n) 
# Space Complexity: O(n)
