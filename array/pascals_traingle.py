#PASCAL'S traingle
class Solution:
    def findPascalElement(self, r, c):
        n = r - 1
        k = c - 1
        res = 1
        for i in range(1, k + 1):
            res = res * (n - i + 1) // i
        return res
#lc 
class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            # start each row with 1
            row = [1]
            # fill middle elements using previous row
            if i > 0:
                for j in range(1, i):
                    row.append(result[i-1][j-1] + result[i-1][j])
                # end each row with 1 (except first row)
                if i > 0:
                    row.append(1)
            result.append(row)
        return result

