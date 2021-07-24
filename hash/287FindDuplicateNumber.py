class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate_set = set()
        for num in nums:
            if num in duplicate_set:
                return num
            duplicate_set.add(num)
        return -1