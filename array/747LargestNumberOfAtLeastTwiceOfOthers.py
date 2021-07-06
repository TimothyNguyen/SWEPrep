def dominantIndex(nums):
    maxIndex = 0
    for i in range(len(nums)):
        if nums[i] > nums[maxIndex]: maxIndex = i
    for i in range(len(nums)):
        if maxIndex != i and nums[maxIndex] < 2 * nums[i]:
            return -1
    return maxIndex