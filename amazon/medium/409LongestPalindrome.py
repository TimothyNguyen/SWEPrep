class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = defaultdict(int)
        for c in s:
            freq_map[c] += 1
        res = 0
        has_odd_frequency = False
        for word in freq_map:
            if freq_map[word] % 2 == 0:
                res += freq_map[word]
            else:
                res += freq_map[word] - 1
                has_odd_frequency = True
        return res + 1 if has_odd_frequency else res

