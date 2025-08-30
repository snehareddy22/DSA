#Counting Frequencies of Array Elements
def Frequency(arr, n):
    mp = {}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    for x in mp:
        print(x, mp[x])


if __name__ == '__main__':
    # Take input from the user
    arr = list(map(int, input("Enter elements of array separated by space: ").split()))
    n = len(arr)
    Frequency(arr, n)
