# Longest Subarray with Sum K (naive, positives & negatives)
def is_subsum(arr, K):
    n = len(arr)
    for i in range(n):            # start index of subarray
        curr_sum = 0              # current sum
        for j in range(i, n):     # end index of subarray
            curr_sum += arr[j]    # add current element
            if curr_sum == K:     # check if sum equals K
                return True
    return False

# Example usage
arr = [int(x) for x in input("Enter array: ").split()]
K = int(input("Enter sum K: "))
print(is_subsum(arr, K))

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Longest Subarray with Sum K (optimal, positives & negatives)
def is_subsum(arr, K):
    prefix_sum = 0
    sum_index = {}  # stores first occurrence of prefix_sum
    for i, num in enumerate(arr):
        prefix_sum += num
        
        if prefix_sum == K:  # subarray from 0 to i
            return True
        
        if (prefix_sum - K) in sum_index:
            return True
        
        if prefix_sum not in sum_index:
            sum_index[prefix_sum] = i  # store first occurrence only
            
    return False

# Example usage
arr = [int(x) for x in input("Enter array: ").split()]
K = int(input("Enter sum K: "))
print(is_subsum(arr, K))

# Time Complexity: O(n) 
# Space Complexity: O(n)
