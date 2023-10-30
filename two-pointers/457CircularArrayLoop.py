class Solution:
    def circularArrayLoop(nums):

        n = len(nums)

        def getIndex(idx):
            # Positive
            if idx + nums[i] >= 0:
                return (idx + nums[i]) % n
            return nums[idx + nums[i]]

        for i in range(n):
            if nums[i] == 0:
                continue
            slow, fast = i, getIndex(i)
            while nums[fast] * nums[i] > 0 and nums[getIndex(fast)] * nums[i] > 0:
                if slow == fast:
                    if slow == getIndex(slow):
                        break
                    return True
                slow = getIndex(slow)
                fast = getIndex(fast)

            slow = i
            val = nums[i]
            while nums[slow] * val > 0:
                next = getIndex(slow)
                nums[slow] = 0
                slow = next
            
        return False