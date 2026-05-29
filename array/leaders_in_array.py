#Leaders in an Array
# Input:arr = [4, 7, 1, 0]
# Output: [7 1 0]
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
    def leaders(self,nums):
        n = len(nums)
        result = []
        max_so_far = float('-inf')
        # traverse from right
        for i in range(n - 1, -1, -1):
            if nums[i] > max_so_far:
                result.append(nums[i])
                max_so_far = nums[i]
        # reverse to maintain order
        return result[::-1]
#TC=O(N)
#SC=O(N)