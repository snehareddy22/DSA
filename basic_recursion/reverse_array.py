# Reverse an array using recurion
#Parameterized Recursion
def reverse_array(arr, i, n):
    if i >= n // 2:   # base case
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]  # swap
    reverse_array(arr, i + 1, n)
arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(arr))
print(arr)   
#Time Complexity: O(n)
#Space Complexity: O(n) (recursion stack)

#2. Functional Recursion
def reverse_array(arr):
    if len(arr) <= 1:   # base case
        return arr
    return reverse_array(arr[1:]) + [arr[0]]
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))   
#Time Complexity: O(n²) (because of slicing)
#Space Complexity: O(n) (stack + new array)



