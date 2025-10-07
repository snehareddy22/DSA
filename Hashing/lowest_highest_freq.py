#Find the highest/lowest frequency element
#LC LINK=https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/1793707872/
#naive approach
def high_low_freq(arr):
    n = len(arr)
    max_freq = 0
    min_freq = n  # start with a large number
    freq_dict = {}  # store element -> frequency
    for i in range(n):
        flag = False  # Check if element is already counted
        for j in range(i):
            if arr[i] == arr[j]:
                flag = True
                break
        if flag:
            continue
        freq = 1  # Count frequency of arr[i]
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                freq += 1
        freq_dict[arr[i]] = freq  # store frequency
        max_freq = max(max_freq, freq)
        min_freq = min(min_freq, freq)
    print("Frequencies of elements:")
    for key, value in freq_dict.items():
        print(key, value)
    print("\nHighest frequency elements:")
    for key, value in freq_dict.items():
        if value == max_freq:
            print(key, value)
    print("\nLowest frequency elements:")
    for key, value in freq_dict.items():
        if value == min_freq:
            print(key, value)
#Time Complexity: O(n²)
#Space Complexity: O(1)

#optimal approach
from collections import Counter
def high_low_freq_optimal(arr):
    # Step 1: Count frequencies automatically
    freq = Counter(arr)
    # Step 2: Find highest and lowest frequency values
    max_freq = max(freq.values())
    min_freq = min(freq.values())
    # Step 3: Print all frequencies
    print("Frequencies of elements:")
    for key, value in freq.items():
        print(key, value)
    # Step 4: Print elements with highest frequency
    print("\nHighest frequency elements:")
    for key, value in freq.items():
        if value == max_freq:
            print(key, value)
    # Step 5: Print elements with lowest frequency
    print("\nLowest frequency elements:")
    for key, value in freq.items():
        if value == min_freq:
            print(key, value)
#Time Complexity: O(n)
##Space Complexity: O(n)

#LC 
class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()  # Sort the array
        left = 0
        total = 0  # Sum of elements in the current window
        result = 0
        for right in range(len(nums)):
            total += nums[right]
            window_size = right - left + 1
            # If total increments needed exceed k, shrink window from left
            while nums[right] * window_size - total > k:
                total -= nums[left]
                left += 1
                window_size -= 1
            # Update max frequency
            result = max(result, window_size)
        return result
sol = Solution()
print(sol.maxFrequency([1,2,4], 5))       # Output: 3
print(sol.maxFrequency([1,4,8,13], 5))   # Output: 2
print(sol.maxFrequency([3,9,6], 2))      # Output: 1

# Time: O(n log n) → sorting + sliding window
# Space: O(1) extra