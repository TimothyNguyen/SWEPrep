def pivotIndex(nums):
    sum, leftSum = 0, 0
    for x in nums: sum += x
    for x in nums:
        if leftSum + x == sum - x: return True
        leftSum += x
        sum -= x
    return False