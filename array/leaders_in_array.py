#Leaders in an Array
#example
# Input:arr = [4, 7, 1, 0]
# Output: 7 1 0
#brute force
def printLeadersBruteForce(arr, n):
    ans = []
    for i in range(n):
        leader = True
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader:
            ans.append(arr[i])
    return ans
#TC=O(N2)
#SC=O(N)

#optimal apprach
class Solution:
    def leaders(self, arr):
        ans = [] 
        n=len(arr)
        leader = arr[n - 1] 
        ans.append(arr[n - 1]) 
        for i in range(n-2, -1, -1): # check from second last to first
            if arr[i] >=leader:
                ans.append(arr[i])
                leader = arr[i]
        ans.reverse() 
        return ans
#TC=O(N)
#SC=O(N)