class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(maxsize = None)
        def dfs(index, s):
            
            if index == len(s):
                return 1
            
            if s[index] == '0':
                return 0
            
            if index == len(s) - 1:
                return 1
            
            answer = dfs(index + 1, s)
            if int(s[index : index + 2]) <= 26:
                answer += dfs(index + 2, s)
            
            return answer
        
        return dfs(0, s)