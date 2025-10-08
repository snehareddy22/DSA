#Find Second Smallest and Second Largest Element in an array
#brute force(if no dup present)
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
arr= list(map(int, input("Enter elements: ").split()))
print(second_largest(arr))

#optimal appraoch
def second_largest_and_smallest(arr):
    if len(arr) <= 1:
        return None   # edge cases
    largest = max(arr)       #find largest element
    smallest = min(arr)      #find smallest element
    seclarge = None  # initialize second largest
    secsmall = None  # initialize second smallest
    # Find second largest
    for x in arr:
        if x != largest:         #check  if i  is equal to largest  if not
            if seclarge is None:
                seclarge = x      #initialize i to seclarge
            else:
                seclarge = max(x, seclarge)    #in sub sequent check the max of i,seclar 
    # Find second smallest
    for x in arr:
        if x != smallest:
            if secsmall is None:
                secsmall = x
            else:
                secsmall = min(x, secsmall)
    return seclarge, secsmall
arr= [int(x) for x in input().split()]
print(second_largest_and_smallest(arr))


#optimal approch(using 1 iteraraion)
def second_largest(arr):
    if len(arr) <= 1:
        return None 
    largest=arr[0]
    second_largest=None
    for i in arr[1:]:
        if i >largest:
            second_largest=largest
            largest=i
        elif i<largest:
            if second_largest is None or i>second_largest:
                second_largest=i
    return second_largest
arr= [int(x) for x in input().split()]
print(second_largest(arr))



