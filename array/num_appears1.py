#Find the number that appears once, and the other numbers twice
#LC CODE:https://leetcode.com/problems/single-number/submissions/1795843057/
#brute force(using loops)
def appear_once(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]   # number appears once
arr = list(map(int, input().split()))
print(appear_once(arr))
# Time complexity: O(n²) 
# Space complexity: O(1)

#optimal approach using EX-OR
#a ⊕ a = 0 
#a ⊕ 0 = a
def appear_once(arr):
    n=len(arr)
    xor=0
    for i in arr:
        xor^=i
    return xor
arr = list(map(int, input().split()))
print(appear_once(arr))
# Time Complexity: O(n)
# Space Complexity: O(1)