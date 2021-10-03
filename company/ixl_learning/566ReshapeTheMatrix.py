class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[0] * c for _ in range(r)]
        if len(nums) == 0 or (r * c != len(nums) * len(nums[0])):
            return nums
        rows, cols = 0, 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                res[rows][cols] = nums[i][j]
                cols += 1
                if cols == c:
                    cols = 0
                    rows += 1
        return res