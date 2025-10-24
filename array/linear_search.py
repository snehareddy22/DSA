# Linear Search
# Example 1:
# Input: arr[]= 1 2 3 4 5, num = 3
# Output: 2
# Example 2:
# Input: arr[]= 5 4 3 2 1, num = 5
# Output: 0
def linear_search(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1
n=int(input())
arr=list(map(int,input().split()))
print(linear_search(arr,n))

#TC=O(n)
#SC=O(1)