class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for num in nums:
            if num in ans: return True
            ans.add(num)
        return False