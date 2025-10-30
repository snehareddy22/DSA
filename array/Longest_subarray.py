#Longest subarray with sum K
# naive(using loops)
def longest_subarray_sum_k(arr,sum) :
    n=len(arr)
    for i in range(n) :        #i for evry elemnet in arr
        curr = 0                      #keep current sum as 0
        for j in range(n) :   #inner loop goes from i to last elemnt
            curr += arr[j]            #add j to the count
            if (curr == sum) :        #if current sum =sum then return it
                return True          
    return False                       
arr =list(map(int,input().split())) 
sum = int(input())
print(longest_subarray_sum_k(arr,sum))
#tc=o(n2)
# sc=o(1)


#optimal approach(sliding window)
def longest_subarray_sum(arr, target):
    s, curr = 0, 0
    for i in range(len(arr)):   # i→ end pointer
        curr += arr[i]          # add current element
        while curr > target and s <= i:   # shrink window if sum exceeds target
            curr -= arr[s]
            s += 1
        if curr == target:   # if we hit the target sum
            print("Subarray with sum", target, "is:", arr[s:i+1])
            return True
    return False  # if no subarray found
arr =list(map(int,input().split())) 
target = int(input())
print(longest_subarray_sum_k(arr,target))
#tc=o(n2)
# sc=o(1)