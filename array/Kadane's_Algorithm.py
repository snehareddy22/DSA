#Kadane's Algorithm : Maximum Subarray Sum in an Array
 #Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

#brute force
import sys
def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  # start with smallest possible number
    for i in range(n):       # check all possible subarrays
        for j in range(i, n):
            summ = 0  # sum of current subarray
            for k in range(i, j + 1):      # calculate sum of subarray arr[i...j]
                summ += arr[k]
            maxi = max(maxi, summ)    # update maximum sum
    return maxi
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)
#TC=O(N³)
#SC=O(1)

#better appraoch
import sys
def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1 
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            maxi = max(maxi, sum)
    return maxi
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)       
#TC=O(N2)
#SC=O(1)

#optimal approach
import sys
def maxSubarraySum(arr, n):
    maxi = -sys.maxsize-1 # maximum sum
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum > maxi:
            maxi = sum
        if sum < 0:  # If sum < 0: discard the sum calculated
            sum = 0
    return maxi
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)
#TC=O(N)
#SC=O(1)