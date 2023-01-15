class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr_list, open, close):
            if len(curr_list) == n*2:
                ans.append(''.join(curr_list))
                return
            if open > 0 and open <= n:
                curr_list.append('(')
                backtrack(curr_list, open + 1, close)
                curr_list.pop()
            if open > close:
                curr_list.append(')')
                backtrack(curr_list, open, close + 1)
                curr_list.pop()
        backtrack([], 1, 1)
        return ans