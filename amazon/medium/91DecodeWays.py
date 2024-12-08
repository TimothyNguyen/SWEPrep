class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def decode(i, s):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s) - 1:
                return 1
            answer = decode(i + 1, s)
            if i < len(s) - 1 and int(s[i:i+2]) <= 26:
                answer += decode(i + 2, s)
            memo[i] = answer
            return answer

        return decode(0, s)