'''
A message containing letters from A-Z can be encoded 
into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
'''
class Solution: 
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def dfs(index, s):
            if index == s:
                return 1
            if s[index] == '0':
                return 0
            if index == len(s) - 1:
                return 1
            answer = dfs(index + 1, s)
            if int(s[index : index + 2]) <= 26:
                answer += dfs(index + 2, s)

        return dfs(0, s)
