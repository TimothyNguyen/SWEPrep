class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def next_permutation(nums: List[int]):
            def reverse(i):
                l, r = i, len(nums) - 1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            i = len(nums) - 2
            while i >= 0 and nums[i + 1] <= nums[i]:
                i -= 1
            if i >= 0:
                j = len(nums) - 1
                while j >= 0 and nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            reverse(i + 1)
        if len(nums) <= 1:
            return [nums]
        set_of_tuples = set()
        while True:
            next_permutation(nums)
            curr_list_to_tuples = tuple(nums)
            if curr_list_to_tuples in set_of_tuples:
                break
            set_of_tuples.add(curr_list_to_tuples)
        ans = [list(t) for t in set_of_tuples]
        return ans
