'''
Given a string s, return the length of the longest substring 
that contains at most two distinct characters.

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
'''
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