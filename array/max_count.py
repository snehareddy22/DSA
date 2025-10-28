#Count Maximum Consecutive One's in the array
def max_count(arr):
    count=0
    max_count=0
    for i in range(len(arr)):
        if arr[i]==1:    #if arr[i] == arr[i-1]: if any Count maximum consecutive equal numbers
            count+=1
            max_count=max(max_count,count)
        else:
            count=0
    return max_count
arr=list(map(int,input().split()))
print(max_count(arr))