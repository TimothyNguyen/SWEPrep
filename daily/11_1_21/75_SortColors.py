# [0, 1, 1, 2, 2, 1, 0, 0, 0, 2]

def dutch_flag_partition(arr):
    l, m, r = 0, 0, len(arr) - 1
    while m <= r:
        if arr[m] == 0:
            arr[m], arr[l] = arr[l], arr[m]
            l += 1
            m += 1
        elif arr[m] == 2:
            arr[m], arr[r] = arr[r], arr[m]
            r -= 1
            m += 1
        else:
            m += 1
    return arr