#Find the highest/lowest frequency element
def highestLowestFreq(arr, n):
    # Step 1: Create an empty dictionary to store frequencies
    freq = {}

    # Step 2: Count frequency of each element
    for i in range(n):
        if arr[i] in freq:              # if element already exists in dictionary
            freq[arr[i]] += 1           # increase its count by 1
        else:
            freq[arr[i]] = 1            # otherwise add it with count 1

    # Step 3: Find element with maximum frequency
    # max(freq, key=freq.get) → looks for the key that has the highest value in dictionary
    max_elem = max(freq, key=freq.get)

    # Step 4: Find element with minimum frequency
    # min(freq, key=freq.get) → looks for the key that has the lowest value in dictionary
    min_elem = min(freq, key=freq.get)

    # Step 5: Print results
    print(max_elem, min_elem)


if __name__ == "__main__":
    # Take input from user
    arr = list(map(int, input("Enter elements: ").split()))
    n = len(arr)
    highestLowestFreq(arr, n)

