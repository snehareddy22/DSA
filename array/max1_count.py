#Count Maximum Consecutive One's in the array
def max_count(arr):
    count=0
    max_count=0
    for i in arr:
        if arr[i]==1:     
            count+=1
            max_count=max(max_count,count)
        else:
            count=0    #if 0 occurs reset count to 0
    return max_count
