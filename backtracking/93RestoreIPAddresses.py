class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s) < 4:
            return ans
        
        def backtrack(arr, curr_idx, has_leading_zero):
            if len(arr) == 4 and curr_idx == len(s):
                for num in range(len(arr)):
                    ans.append(num)
                return
            for i in range(len(s)):
                if len(arr) < 4:
                    if s[curr_idx] != '0' or not has_leading_zero:
                        arr.append(s[curr_idx])
                        backtrack(arr, curr_idx + 1, (has_leading_zero or s[curr_idx] == '0'))
                        arr.pop()
                    arr[-1] += s[curr_idx]
                    backtrack(arr, curr_idx + 1, has_leading_zero)
                    arr.pop()
        return ans

                    
                        