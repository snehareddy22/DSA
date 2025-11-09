#Rearrange Array Elements by Sign
#brute force
class Solution:
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        # Separate positives and negatives
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        res = []
        # Alternate between positive and negative
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res
#TC=O(n)
#SC=O(n)

#optimal approach
class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        res = [0] * n  # just to rearrange positions
        posIndex = 0   # even index → positive
        negIndex = 1   # odd index → negative
        for num in nums:
            if num > 0:
                res[posIndex] = num
                posIndex += 2
            else:
                res[negIndex] = num
                negIndex += 2   
        return res
#TC=O(n)
#SC=O(1)