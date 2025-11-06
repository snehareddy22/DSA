#Find the Majority Element that occurs more than N/2 times
def majorityElement(arr):
    n = len(arr)
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j] == arr[i]:
                cnt += 1
        if cnt > (n // 2):  # Check if frequency is greater than n/2
            return arr[i]
    return -1
n=int(input())
arr=list(map(int,input().split()))
#TC=O(2n)
#SC=O(n)


#better(using hashmap)
from collections import Counter
def majorityElement(arr):
    n = len(arr)
    counter = Counter(arr)
    for num, count in counter.items():
        if count > (n // 2):
            return num
    return -1
n=int(input())
arr=list(map(int,input().split()))
#TC=O(N2)
#SC=O(n)


#optimal approach(using Moore’s Voting Algorithm)
def majority_element(arr):
    candidate = None   # Step 1: Find the candidate element
    count = 0
    for num in arr:
        if count == 0:
            candidate = num    # choose a new candidate
        if num == candidate:
            count += 1         # same as candidate, increase count
        else:
            count -= 1         # different, decrease count
    if arr.count(candidate) > len(arr) // 2:  # Step 2: Verify candidate using count()
        return candidate
    else:
        return "No Majority Element"
arr = [2, 2, 1, 1, 1, 2, 2]
print("Majority Element:", majority_element(arr))

