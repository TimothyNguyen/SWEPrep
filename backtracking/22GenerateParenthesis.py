class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def backtracking(open_b, close_b, i, n, path):
            if i == n * 2:
                ans.append("".join(path))
                return
            
            if open_b > 0:
                path.append('(')
                backtracking(open_b - 1, close_b, i + 1, n, path)
                path.pop()
            if open_b < close_b:
                path.append(')')
                backtracking(open_b, close_b - 1, i + 1, n, path)
                path.pop()
            
            
        backtracking(n, n, 0, n, [])
        return ans