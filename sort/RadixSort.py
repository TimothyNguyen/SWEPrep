def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * n    # output has sorted array
    count = [0] * 10 

    # Store the occurrences in count[]
    for i in range(n):
        index = arr[i] / exp1
        count[int(index % 10)] += 1
    
    # Change count[i] so that count[i] contains actual 
    # position of this digit in output array
    for i in range(1, 10): count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] / exp1
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
    
    i = 0
    for i in range(len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)
    # Do sorting count for every digit
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10