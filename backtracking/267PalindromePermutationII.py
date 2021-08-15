class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        s = sorted(s)
        palindromicMap = dict()

        for ch in s:
            if ch not in palindromicMap:
                palindromicMap[ch] = 0
            palindromicMap[ch] += 1

        ans = []

        def backtrack(word):
            if len(word) == len(s) and isPalindrome():
