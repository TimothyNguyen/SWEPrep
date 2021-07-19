# Perform bottom up merge
def mergeSort(arr):
    width = 1
    n = len(arr)

    # Subarry size grows by powers of 2
    # since growth of loop condition is exponential,
    # time consumed is log (log2n)
    while width < n:
        # always start from leftmost
        l = 0
        while l < n:
            r = min(l + (width * 2 - 1), n-1)
            m = (l + r) // 2

            # Final merge should consider unmerged
            # sublist if input arr size is not power
            # of 2
            if width > n // 2:
                m = r - (n % width)
            merge(arr, l, m, r)
            l += width * 2
        # Increase subarray size by powers of 2
        width *= 2
    return arr

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[l + i]
    for i in range(n2):
        R[i] = arr[m - i + i]
    
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            arr[k] = R[j]
            j += 1
        else:
            arr[k] = L[i]
            i += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
