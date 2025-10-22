#Left Rotate the Array by One

#brute force
def solve(arr, n):
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]
    for i in range(n):
        print(temp[i], end=" ")
# Time Complexity: O(n)
# Space Complexity: O(n)


#optimal approch
def left_rotate(arr):
    last=arr[0]     #store first element
    n=len(arr)
    for i in range(1,n):
        arr[i-1] = arr[i]    #shift all elemnts to left by 1 place
    arr[-1]=last              #place first elment at last
    return arr
arr=list(map(int,input().split()))
print(left_rotate(arr))

# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation: You modify the array directly — no extra array used.



