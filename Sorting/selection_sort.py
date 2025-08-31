#selection sorting(ao)
def selection_sort(arr):
    n=len(arr)
    for i in range(n):#assume index 0 is min value
        min_num=i
        for j in range(i+1,n):   #from second elemnt to exclude last element 
            if arr[j]<arr[min_num]: #find actual min
                min_num=j
        arr[i],arr[min_num]=arr[min_num],arr[i] #swap them
arr=list(map(int,input("enter array elemnts").split()))
selection_sort(arr)
print(arr)