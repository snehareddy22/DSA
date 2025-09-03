#Find the Largest element in an array


# Problem Statement: Given an array, we have to find the largest element in the array.

# Brute Force Approach
# We can sort the array in ascending order, hence the largest element will be at the last index of the array. 
# Approach:Sort the array in ascending order,Print the (size of the array -1)th index.
# DryRun: Before sorting: arr[] = {2,5,1,3,0},After sorting: arr[] = {0,1,2,3,5},answer : arr[sizeofthearray-1] =5

def largest_number(arr):
    arr.sort()
    return arr[-1]
arr=[1,5,3,4,6,3]
print("this is the largest element",largest_number(arr))
# Total Time Complexity = O(n log n)
# Python’s sort() is implemented as Timsort, which uses O(n) worst-case auxiliary space.

# Recursive Approach

# We can maintain a max variable that will update whenever the current value is greater than the value in the max variable.  
# Approach:Create a max variable and initialize it with arr[0],Use a for loop and compare it with other elements of the array,
# If any element is greater than the max value, update max value with the element’s value,Print the max variable.

def largest_number(arr,n):
    max=arr[0]
    for i in range(0,n):
        if max<arr[i]:
            max=arr[i]
    return max
arr=[4,5,6,24,5,61]
n=len(arr)
largest_number(arr,n)
# Time Complexity=O(n)
# space complexity=O(1)