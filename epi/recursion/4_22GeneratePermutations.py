class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans: List[str] = []
        self.backtrack("", ans, 0, 0, n)
        return ans

    def backtrack(self, s: str, l: List[str], open: int, close: int, max: int):
        if len(s) == max * 2:
            l.append(s)
            return
        if open < max: 
            self.backtrack(s + "(", l, open + 1, close, max)
        if close < open:
            self.backtrack(s + ")", l, open, close + 1, max)
