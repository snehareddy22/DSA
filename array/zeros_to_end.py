#Move all Zeros to the end of the array
#brute force
def move_zeros_bruteforce(arr):
    temp = []
    for  i in arr:                   # Step 1: store non-zero elements
        if i != 0:
            temp.append(i)
    zeroes = len(arr) - len(temp)    # Step 2: count how many zeros
    for i in range(zeroes):           # Step 3: append zeros
        temp.append(0)
    for i in range(len(arr)):         # Step 4: copy back to original array
        arr[i] = temp[i]
#tc=o(n)
#SC=o(n)

#LC
class Solution:
    def moveZeroes(self, nums):
        # j points to the position where next non-zero should go
        j = 0
        # Loop through each element in the array
        for i in range(len(nums)):
            # If current element is non-zero
            if nums[i] != 0:
                # Swap with the element at index j
                nums[i], nums[j] = nums[j], nums[i]

                # Move j forward
                j += 1
#TC=O(n)
#SC=O(1)

