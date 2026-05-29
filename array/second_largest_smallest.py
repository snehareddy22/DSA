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





def second_smallest_largest(arr):
    if len(arr) < 2:
        return None, None
    smallest = float('inf')
    second_smallest = float('inf')
    largest = float('-inf')
    second_largest = float('-inf')
    for i in arr:
        # For smallest & second smallest
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif smallest < i < second_smallest:
            second_smallest = i

        # For largest & second largest
        if i > largest:
            second_largest = largest
            largest = i
        elif second_largest < i < largest:
            second_largest = i

    # if duplicates caused no valid second values
    if second_smallest == float('inf') or second_largest == float('-inf'):
        return None, None

    return second_smallest, second_largest




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
