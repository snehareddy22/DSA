#Longest subarray with sum K
# naive(using loops)
def longest_subarray_sum_k(arr, k):   #checking possible  sub arrays 
    n = len(arr)
    lenght=0                          #initialize lenth
    for i in range(n):                #outer loop
        curr = 0                      #keep current sum as 0
        for j in range(i, n):         #inner loop
            curr += arr[j]            # add element arr[j] to current sum
            if curr == k:             #if sum is euaqual to the given k
                lenght=max(lenght,j-i+1)   #check for the max lenght array which satisfies  curr == k
    return lenght                      #return that lenght
arr = list(map(int, input().split()))
k = int(input())
print(longest_subarray_sum_k(arr, k))
#tc=o(n2)
# sc=o(1)


#optimal approach(sliding window)
def longest_subarray_sum(arr, target):
    s, curr = 0, 0           # s → start pointer, curr → current sum
    max_len = 0
    for i in range(len(arr)):   # i → end pointer
        curr += arr[i]          # include arr[i] in current window
        # shrink window if sum exceeds target
        while curr > target and s <= i:
            curr -= arr[s]
            s += 1
        # check if sum equals target
        if curr == target:
            max_len = max(max_len, i - s + 1)
    return max_len
arr =list(map(int,input().split())) 
target = int(input())
print(longest_subarray_sum_k(arr,target))
#tc=o(n)
# sc=o(1)

