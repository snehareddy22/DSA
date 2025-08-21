# Reverse an array

def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")   # print each element in the array
    print()  # new line after printing


# Function to reverse an array (iterative approach with extra array)
def reverseArray(arr, n):
    ans = [0] * n   # create a new array "ans" of size n (initially all 0s)
    
    # Traverse the array backward
    for i in range(n - 1, -1, -1):     # i goes from n-1 down to 0
        ans[n - i - 1] = arr[i]        # fill ans from left to right
    
    # Print the reversed array
    printArray(ans, n)


# Driver Code
arr = [5, 4, 3, 2, 1]
n = len(arr)
reverseArray(arr, n)   # Output: 1 2 3 4 5



# or


# Function to print an array
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")   # print each element
    print()


# Recursive function to reverse an array in-place
def reverseArray(arr, start, end):
    # Base case: when start index meets or crosses end index, stop recursion
    if start >= end:
        return
    
    # Swap the elements at start and end
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recursive call for the remaining middle part
    reverseArray(arr, start + 1, end - 1)


# Driver Code
arr = [5, 4, 3, 2, 1]
n = len(arr)

reverseArray(arr, 0, n - 1)   # Call recursion with start=0 and end=n-1
printArray(arr, n)            # Output: 1 2 3 4 5
