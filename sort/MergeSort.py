def merge(list1, list2):
    if len(list1) == 0: return list2
    if len(list2) == 0: return list1
    if list1[0] < list2[0]: return list1[0] + merge(list1[1:], list2)
    else: return list2[0] + merge(list1, list2[1:])

def merge_sort(nums):
    if not nums or len(nums) <= 1 : return nums
    m = len(nums) // 2
    l = merge_sort(nums[:m])
    r = merge_sort(nums[m:])
    return merge(l, r)