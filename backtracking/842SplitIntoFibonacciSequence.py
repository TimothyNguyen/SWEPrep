class Solution:
    def splitIntoFibonacci(self, ans: str) -> List[int]:
        def backtrack(s, result, idx):
            if len(s) == idx: return len(result) > 2
            num = 0
            for i in range(idx, len(s)):
                num = (num * 10) + int(s[i])
                #if num < 0: return False
                if len(result) < 2 or result[-1] + result[-2] == num:
                    result.append(num)
                    if backtrack(s, result, i + 1): 
                        return True
                    result.pop()
                if i == idx and s[i] == '0': 
                    return False
            return False
        
        result = []
        backtrack(ans, result, 0)
        return result
                    