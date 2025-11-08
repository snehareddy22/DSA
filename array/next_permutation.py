#next permutation find next lexicographically greater permutation
#bruteforce
from itertools import permutations
class Solution:
    def nextPermutation(self, nums):
        perms = sorted(set(permutations(nums))) # Generate all unique permutations
        current = tuple(nums)                   # Convert list to tuple for comparison
        for i in range(len(perms)):             # Traverse the list
            if perms[i] == current:              # If last permutation, return first
                if i == len(perms) - 1:
                    return list(perms[0])         # Else return next
                return list(perms[i + 1])
        return nums
sol = Solution()
nums = [1, 2, 3]
result = sol.nextPermutation(nums)
print(" ".join(map(str, result)))

# Complexity
# TC= O(N!*N)
#SC=O(N!)
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # Step 1: Find first decreasing element from end
            i -= 1
        if i >= 0:                                # Step 2: Find just larger element to the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # swap
        nums[i + 1:] = reversed(nums[i + 1:])    # Step 3: Reverse the suffix
        return nums  
# Complexity:
#  Time: O(n)
#  Space: O(1)