class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, curr_result, curr_num):
            if curr_num == target:
                ans.append(list(curr_result))
                return
            if i >= len(candidates) or curr_num > target:
                return
            for idx in range(i, len(candidates)):
                num = candidates[idx]
                if curr_num + num <= target:
                    curr_result.append(num)
                    dfs(idx + 1, curr_result, curr_num + num)
                    curr_result.pop()
                else:
                    continue
        ans = []
        dfs(0, [], 0)
        return ans
