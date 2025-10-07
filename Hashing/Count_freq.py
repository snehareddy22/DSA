#Counting Frequencies of Array Elements
#naive approach
def count_freq(arr, n):
    for i in range(n):
        flag = False    #we assume this element has not appeared before.
        # check if this element has already appeared
        for j in range(i):
            if arr[i] == arr[j]:
                flag = True   #skip counting this element (because it’s already been counted earlier).
                break
        if flag:              #if already appreaed ignore it
            continue
        freq = 1               #if not seen count frequency
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                freq += 1
        print(arr[i], freq)
n=int(input())
arr = list(map(int, input("Enter elements: ").split()))
print(count_freq(arr,n))

#eg arr = [10, 20, 10, 30],  n = 4
# i = 0 → element = 10
# No previous elements → count frequency → appears 2 times → print 10 2
# i = 1 → element = 20
# Not seen before → count frequency → appears 1 time → print 20 1
# i = 2 → element = 10
# Already seen at i = 0 → skip
# i = 3 → element = 30
# Not seen before → count frequency → appears 1 time → print 30 1

#TC=O(n2)  
#First inner loop (for j in range(i)) → in the worst case runs up to O(n)
#Second inner loop (for j in range(i+1, n)) 
#SC=O(1)


#optimal approach
def count_freq(arr, n):
    hmp=dict()              #dictionary (hashmap) to store frequencies
#Step 1: count frequencies
    for i in range(n):
        if arr[i] in hmp.keys():      # if element already in dictionary
            hmp(arr[i])+=1            # increment its count
        else:
            hmp[arr[i]]=1             #other wise cnt is 1 
    for x in hmp:
        print (x," ",hmp[x])
#[10, 20, 10, 30, 20, 10]
# See 10 → not in dict → {10: 1}
# See 20 → not in dict → {10: 1, 20: 1}
# See 10 → already in dict → {10: 2, 20: 1}
# See 30 → not in dict → {10: 2, 20: 1, 30: 1}
# See 20 → already in dict → {10: 2, 20: 2, 30: 1}
# See 10 → already in dict → {10: 3, 20: 2, 30: 1}
# o/p:10 3
#     20 2
#     30 1
#tc=o(n)
#sc=o(n)

#using counter
from collections import Counter
def count_freq_counter(arr):
    freq = Counter(arr) #Counter(arr) automatically counts how many times each element appears.
    for key, value in freq.items():
        print(key, value)
arr = list(map(int, input("Enter elements: ").split()))
count_freq_counter(arr)
#tc=o(n)
#sc=o(n)

