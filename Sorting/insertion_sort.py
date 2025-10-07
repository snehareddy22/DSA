#Insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]       # element to be inserted
        j = i - 1
        # shift elements of the sorted part to the right if they are bigger than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key   # insert key at correct position
arr = list(map(int, input("Enter array elements separated by space: ").split()))
insertion_sort(arr)
print("Sorted array:", arr)

#tc=o(n2)