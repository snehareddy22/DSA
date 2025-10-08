#Union of Two Sorted Arrays
#brute force
def find_union(arr1, arr2):
    freq = {}       #to store number of times a element occur
    union = []      #to store arrs union
    for i in arr1:
        freq[i] = freq.get(i, 0) + 1
    for i in arr2:
        freq[i] = freq.get(i, 0) + 1 #freq.get(i, 0)returns current count if exists, else 0.
    for i in freq:
        union.append(i)
    return union
arr1 = list(map(int, input("Enter elements: ").split()))
arr2 = list(map(int, input("Enter elements: ").split()))
print(find_union(arr1,arr2))
#TC=O(n + m)
#sc=O(n + m)

#optimal aproach
def find_union(arr1, arr2):
    s = set()        #create a empty set
    union = []       #create an empty union list
    for i in arr1:   #add arr1 element to set
        s.add(i) 
    for i in arr2:
        s.add(i)     #add arr2 element to set
    for i in s:
        union.append(i)   #add set elements to union becouse set in onodered and canot call by index
    return union
arr1 =list(map(int, input("Enter elements: ").split()))
arr2 =list(map(int, input("Enter elements: ").split())) 
print(find_union(arr1, arr2))

