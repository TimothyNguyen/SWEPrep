class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s) * k == 0: return 0
        l, r = 0, 0
        max_num = 1
        hashmap = dict()
        while r < len(s):
            hashmap[s[r]] = r
            r += 1
            if len(hashmap) == k + 1:
                # Delete the leftmost character
                delidx = min(hashmap.values())
                hashmap.pop(s[delidx])
                l = delidx + 1
            max_num = max(max_num, r - l)
        return max_num