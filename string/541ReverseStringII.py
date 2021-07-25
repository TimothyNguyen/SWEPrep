class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans, reverse = "", True
        for i in range(0, len(s), k):
            if reverse: ans += s[i:i+k][::-1]
            else: ans += s[i:i+k]
            reverse = not reverse
        return ans