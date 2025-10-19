#Longest subarray with sum K
# naive
def is_subsum(arr,sum) :
    for i in range(len(arr)) :        #i for evry elemnet in arr
        curr = 0                      #keep current sum as 0
        for j in range(i,len(arr)) :   #inner loop goes from i to last elemnt
            curr += arr[j]            #add j to the count
            if (curr == sum) :        #if current sum =sum then return it
                return True          
    return False                       
arr =[int(x) for x in input().split()] 
sum = int(input())
print(is_subsum(arr,sum))
#tc=o(n2) sc=o(1)

#optimal approach
# Subarray with Given Sum
# Efficient
def issubsum(arr,sum) :
    s, curr = 0, 0
    for i in range(len(arr)) :
        curr += arr[i]
        while (curr > sum) :
            curr -= arr[s]
            s += 1 
        if (curr == sum) :
            return True
    return False
arr = [int(x) for x in input().split()] 
sum = int(input())
print(issubsum(arr, sum))
