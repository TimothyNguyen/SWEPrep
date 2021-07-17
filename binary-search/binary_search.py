def binary_search(arr, key):
    return recursive_binary_search(arr, key, 0, len(arr))

def recursive_binary_search(arr, key, l, r):
    m = l + (r - l) / 2
    if l == r: return None
    if arr[m] == key: return m
    elif arr[m] < key: binary_search(arr, key, m + 1, r)
    else: binary_search(arr, key, l, m)

def binary_iterative_search(arr, key):
    l, r = 0, len(arr)
    while l <= r:
        m = l + (r - l) / 2
        if arr[m] > key: r = m
        elif arr[m] < key: l = m + 1
        else: return m
    return None
