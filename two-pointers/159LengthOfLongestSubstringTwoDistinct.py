class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2: return len(s)
        l, r = 0, 0
        max_num = 2
        hashmap = dict()
        while r < len(s):
            hashmap[s[r]] = r
            r += 1
            if len(hashmap) == 3:
                # Delete the leftmost character
                delidx = min(hashmap.values())
                hashmap.pop(s[delidx])
                l = delidx + 1
            max_num = max(max_num, r - l)
        return max_num