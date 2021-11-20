# [0, 1, 2, 3, 0, 3, 0, 1, 2, 3, 3, 3, 3, 3, 0, 0, 0, 0, 2, 2, 0, 0, 1, 1, 0, 1, 1, 0, 0]
#     i  j  k                                                                          l
def four_colored_sort(arr):
    i, j, k, l = 0, 0, 0, len(arr) - 1
    # Set them in right positions
    while arr[i] == 0:
        i += 1
        j = i 
        k = i
    while arr[j] == 1:
        j += 1 
        k = j
    while arr[k] == 2: 
        k += 1
    while arr[l] == 3:
        l -= 1
    
    while k <= l:
        if arr[k] == 0: # swap with arr[i] if 0 is found
            arr[i], arr[k] = arr[k], arr[i]
        elif arr[k] == 1: # Swap with arr[j] if 1 if found
            arr[j], arr[k] = arr[k], arr[j]
        elif arr[k] == 3:
            arr[l], arr[k] = arr[k], arr[l]

        while arr[i] == 0:
            i += 1
            j = i 
            k = i
        while arr[j] == 1:
            j += 1 
            k = j
        while arr[k] == 2: 
            k += 1
        while arr[l] == 3:
            l -= 1
    return arr