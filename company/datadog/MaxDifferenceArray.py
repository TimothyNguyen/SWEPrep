def maxAbsDiff(arr, n):
 
    # To store the minimum and the maximum
    # elements from the array
    minEle = arr[0]
    maxEle = arr[0]
    for i in range(1, n):
        minEle = min(minEle, arr[i])
        maxEle = max(maxEle, arr[i])
 
    return (maxEle - minEle)