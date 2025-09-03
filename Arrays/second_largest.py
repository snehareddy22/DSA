#Find Second Smallest and Second Largest Element in an array
#Problem Statement: Given an array, find the second smallest and second largest element in the array.
#  Print ‘-1’ in the event that either of them doesn’t exist.
''''
Brute Force Approach
Solution 1: (Brute Force) [this approach only works if there are no duplicates]
What do we do to find the largest or the smallest element present in an array? We ideally sort them and the first 
element would be the smallest of all while the last element would be the largest. Can we find the second-smallest
 and second-largest
Sort the array in ascending order,The element present at the second index is the second smallest element,
The element present at the second index from the end is the second largest element
'''
def second_element(arr,n):
    arr.sort()
    second_small_element=arr[1]
    second_large_element=arr[n-2]
    return second_small_element,second_large_element
arr=[2,3,5,2,9,3]
n=len(arr)
second_small_element,second_large_element = second_element(arr, n)
print("the second largest element is:",second_large_element)
print("the second smallest element is:",second_small_element)

# Time Complexity: O(NlogN), For sorting the array
# Space Complexity: O(1)
'''
Optimal Approach
We would require four variables: small,second_small, large, and second_large. Variable small and 
second_small are initialized to INT_MAX while large and second_large are initialized to INT_MIN.
Second Smallest Algo:
If the current element is smaller than small then we update second_small and small variables
Else if the current element is smaller than second_small then we update the variable second_small
Once we traverse the entire array, we would find the second smallest element in the variable second_small.
Second Largest Algo:
If the current element is larger than large then update second_large and large variables
Else if the current element is larger than second_large then we update the variable second_large.
Once we traverse the entire array, we would find the second largest element in the variable second_large.
'''  
import sys
def second_smallest_largest(arr, n):
    small = second_small = sys.maxsize   # INT_MAX
    large = second_large = -sys.maxsize  # INT_MIN
    for i in range(n):
        if arr[i] < small:      # Smallest and Second Smallest 
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > large:     # Largest and Second Largest
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    return second_small, second_large

arr = [2, 3, 5, 2, 9, 3]
n = len(arr)
second_small, second_large = second_smallest_largest(arr, n)
print("The second smallest element is:", second_small)
print("The second largest element is:", second_large)


# Time Complexity = O(n) → single pass through the array  ------o(2n)
# Space Complexity = O(1) → only a few variables used
