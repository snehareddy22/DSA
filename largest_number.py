#Find The Largest Element In An Array
#naive solution
def largest_element(arr):
    for i in arr:          #loop an element at a time
        for j in arr:      #check evry nuber in array for i
            if j>i:        #if j>i
                break      #i is not the largest number
            else:          #if it doesnt break
                return i   #return i as the largest number
    return None            
arr= list(map(int, input("Enter elements: ").split()))
print(largest_element(arr))
#TC=O(n2)   becouse we run two loops inner loop and outer loop


#optimal approach
def largest_element(arr):
    if not arr:                #check if the list is empty ot not
        return None
    else:                    #if not cotinue
        res=arr[0]           #assume first element as largest
        for i in range(1,len(arr)):   #check from seconf elemnt to last element
            if arr[i]>res:            #if i is larger than the res
                res=arr[i]            #place i in res and continue
        return res                    #return res
arr= list(map(int, input("Enter elements: ").split()))
print(largest_element(arr))
