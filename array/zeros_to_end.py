#Move all Zeros to the end of the array
#brute force
def move_zeros(arr):
    n=len(arr)
    temp=[]
    # Step 1: Copy non-zero elements to temp
    for i in range(0,n):
        if arr[i]!=0:
            temp.append(arr[i])
    # Step 2: Copy back non-zero elements
    for i in range(len(temp)):
        arr[i] = temp[i]
    # Step 3: Fill remaining places with zeros
    for i in range(len(temp), n):
        arr[i] = 0
    return arr
arr=list(map(int,input().split()))
print(move_zeros(arr))
#TC=o(n)
#SC=o(n)

#optimal approach
def move_zeros(arr):
    n=len(arr)
    j=-1              #keep j as pointer 
    for i in range(n):
        if arr[i]==0:   #check first 0 in the array
            j=i         #keep it in j 
            break       #stop after finding first zero
    if j == -1:         #if there are no zeros return(edge case)
        return arr
    for i in range(j+1, n):  #now check i=j+1 means next elemnt 
        if arr[i] != 0:      #if it is not zero
            arr[i], arr[j] = arr[j], arr[i]    #swap them
            j += 1                             #now run the loop after moving one zero to end go to other zero
    return arr
arr=list(map(int,input().split()))
print(move_zeros(arr))




#LC
class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0  # position to place the next non-zero
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]  # swap
                j += 1
        return nums 
sol=Solution()
print(sol.moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(sol.moveZeroes([0]))               # [0]
#TC=O(n)
#SC=O(1)

