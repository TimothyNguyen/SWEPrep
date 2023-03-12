# Python3 program of Quick Select
'''
function quickSelect(list, left, right, k)

if left = right
      return list[left]

Select a pivotIndex between left and right

pivotIndex := partition(list, left, right, 
                                  pivotIndex)
   if k = pivotIndex
      return list[k]
   else if k < pivotIndex
      right := pivotIndex - 1
   else
      left := pivotIndex + 1 
'''
# Standard partition process of QuickSort(). 
# It considers the last element as pivot 
# and moves all smaller element to left of 
# it and greater elements to right
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthSmallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        pivotIndex = partition(arr, l, r)
        if pivotIndex - l == k - 1:
            return arr[k]
        elif pivotIndex - l < k - 1:
            return kthSmallest(arr, pivotIndex + 1, r, k - pivotIndex + l - 1)
        else:
            return  kthSmallest(arr, l, pivotIndex - 1, k)
arr = [ 10, 4, 5, 8, 6, 11, 26 ]
n = len(arr)
k = 3
print(kthSmallest(arr, 0, n - 1, k))
