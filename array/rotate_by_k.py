#Rotate array by K elements
#Bruteforce
#left rotate by k elemnts
def left_rotatek(arr,k):
    n=len(arr)
    k=k%n    #egde case if k>n
    temp=arr[:k] #Copy first k elements
    for i in range(k,n):
        arr[i-k]=arr[i]   #Shift remaining elements to the left
    arr[:k]=temp        # Copy temp at the end
    return arr
k=int(input())
arr=list(map(int,input().split()))

#right rotate by k elements
def right_rotatek(arr,k):
    n=len(arr)
    k=k%n                      #edge case if k > n
    temp=arr[:k]               #Copy last k elements
    for i in range(n-k-1,-1,-1):  # Shift the first n-k elements to the right
        arr[i+k]=arr[i]
    arr[:k]=temp                #Place the k elements at the beginning
    return arr
k=int(input())
arr=list(map(int,input().split()))

#TC=o(n)
#SC=o(n)

#optimal appraoch(using reversal func)
#left rotate
def left_rotate(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]
# Example
arr = [1, 2, 3, 4, 5, 6, 7]
print(left_rotate(arr, 2))   # Output: [3, 4, 5, 6, 7, 1, 2]


#right roate
def right_rotate(arr, k):
    n = len(arr)
    k = k % n  # handle k > n
    return arr[-k:] + arr[:-k]
# Example
arr = [1,2,3,4,5,6,7]
print(right_rotate(arr, 2))  # Output: [6,7,1,2,3,4,5]

# Example
arr = [1, 2, 3, 4, 5, 6, 7]
print(right_rotate(arr, 2))  # Output: [6, 7, 1, 2, 3, 4, 5]

# arr[-k:] → last k elements → move to front
# arr[:-k] → rest of the array → shift right
#TC=o(n)
#sc=o(1)

#LC 
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n                        #edge case
        nums[:] = nums[-k:] + nums[:-k]  # in-place update
sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
sol.rotate(nums, k)
print(nums)  
nums = [-1,-100,3,99]
k = 2
sol.rotate(nums, k)
print(nums)  
