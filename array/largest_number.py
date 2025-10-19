#Find The Largest Element In An Array

#bruteforce using sorting technique
def largest_element(arr):
    arr.sort()
    print(arr[-1])
arr=list(map(int, input().split()))
largest_element(arr)

#Time Complexity (TC)=o(nlogn)  becouse of sorting operation
#space complexity(sc)-o(1)


#optimal approach creating a max  varibale 
def largest_element(arr):
    max_element=arr[0]
    n=len(arr)
    for i in range(1,n):
        if arr[i]>max_element:
            max_element=arr[i]
    return max_element
arr=list(map(int,input().split()))
print(largest_element(arr))

#Time complexity(tc)-o(n)
#space complexity(sc)-o(1)




