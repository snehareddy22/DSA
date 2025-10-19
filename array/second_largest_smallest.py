#Find Second Smallest and Second Largest Element in an array
#brute force(if no duplicates are  present)
def second_largest(arr):
    n=len(arr)
    arr=sorted(arr)   #sort the array in ascending order
    seclargest=arr[n-2]    #second seclargest number
    return seclargest
arr= list(map(int, input("Enter elements: ").split()))
print(second_largest(arr))

def second_smallest(arr):
    n=len(arr)
    arr=sorted(arr)   #sort the array in ascending order
    secsmallest=arr[1]    #second secsmallest number
    return secsmallest
arr = list(map(int, input("Enter elements: ").split()))
print(second_largest(arr))
#TC=O(nlogn)
#SC=O(1)




#optimal appraoch(using two iterations)
def second_largest_and_smallest(arr):
    if len(arr) <= 1:
        return None   # edge cases
    largest = max(arr)       #find largest element
    smallest = min(arr)      #find smallest element
    seclarge = None  # initialize second largest
    secsmall = None  # initialize second smallest
    # Find second largest
    for i in arr:
        if i != largest:         #check  if i  is equal to largest  if not
            if seclarge is None:
                seclarge = i     #initialize i to seclarge
            else:
                seclarge = max(i, seclarge)    #in sub sequent check the max of i,seclar 
    # Find second smallest
    for i in arr:
        if i != smallest:
            if secsmall is None:
                secsmall = i
            else:
                secsmall = min(i, secsmall)
    return seclarge, secsmall
arr = list(map(int, input("Enter elements: ").split()))
print(second_largest_and_smallest(arr))
# Time Complexity: O(n)
# Space Complexity: O(1)





#optimal approch(using 1 iteraraion)
def second_largest(arr):
    if len(arr) <= 1:     #edgecase
        return None 
    largest=arr[0]       #assume largest=first elemnt
    second_largest=None   #initialize second largest
    for i in arr[1:]:      #start loop from 1 to n
        if i >largest:     #if i is larger than largest elemnt
            second_largest=largest            #largest is kept in second largest
            largest=i                         #i is kept in largest
        elif i<largest:     #if i is smaller than largest
            if second_largest is None or i>second_largest:   #largest will not change
                second_largest=i                             #i is kept in seocond largest
    return second_largest
arr = list(map(int, input("Enter elements: ").split()))
print(second_largest(arr))

#TC=o(n)
#SC=o(1)




def second_largest_and_smallest(arr):
    if len(arr) < 2:
        return None, None
    largest = smallest = arr[0]
    seclargest = secsmall = None
    for i in arr[1:]:
        # For largest
        if i > largest:
            seclargest = largest
            largest = i
        elif i < largest:
            if seclargest is None or i > seclargest:
                seclargest = i
        # For smallest
        if i < smallest:
            secsmall = smallest
            smallest = i
        elif i > smallest:
            if secsmall is None or i < secsmall:
                secsmall = i
    return seclargest, secsmall
arr = [int(x) for x in input().split()]
print(second_largest_and_smallest(arr))
