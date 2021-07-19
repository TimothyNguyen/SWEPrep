def selection_sort(nums):
    for i in range(len(nums) - 1):
        minIdx = i
        for j in range(i+1, len(nums)):
            minIdx = j if nums[j] < nums[i] else minIdx
        nums[minIdx], nums[i] = nums[i], nums[minIdx]
    return nums