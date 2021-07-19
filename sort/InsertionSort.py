def insertSort(nums):
    for i in range(1, len(nums)):
        j = i
        key = nums[i]
        while j > 0 and key < nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        nums[j-1] = key
    return nums