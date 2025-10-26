#Union of Two Sorted Arrays
#using sets(uniion())
def union_array(arr1,arr2):
    return list(set(arr1).union(set(arr2)))   #convert into list and do union ()func
arr1=list(map(int,input().spliit()))
arr2=list(map(int,input().split()))
print(union_array(arr1,arr2))
#Time Complexity:O(n + m)   Converting both lists to sets
#Space Complexity:O(n + m)

#using sets(loops)
def union_array(arr1,arr2):
    s=set()
    union=[]
    for i in arr1:   #add arr1 elemtnt in set
        s.add(i) 
    for i in arr2:   #add atrr2 element in set
        s.add(i)
    for i in range(s):
        union.append(i)     #add set elemnts to union
    return union
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(union_array(arr1,arr2))
#Time Complexity:O(n + m)  
#Space Complexity:O(n + m)



def union_array(arr1a,rr2):
    i, j = 0, 0   #i → pointer for arr1 ,j → pointer for arr2
    union = []    #store unique elements in sorted order
    while i < len(arr1) and j < len(arr2):  #Keep looping as long as both arrays have elements left
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
            #We only add to union if the last element in union is not equal to the new element
                union.append(arr1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
    #Handle leftover elements
    while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    return union
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(union_array(arr1,arr2))


#Time Complexity: O(m + n) → linear through both arrays.
# Space Complexity: O(m + n) → for the union array.