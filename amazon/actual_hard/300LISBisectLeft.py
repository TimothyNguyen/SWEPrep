class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            pos = bisect.bisect_left(sub, x)
            if pos == len(sub):
                sub.append(x)
            else:
                sub[pos] = x
        return len(sub)

'''
[10,9,2,5,3,7,101,18]

[10]
[9]
[2]
[2, 5]
[2, 3]
[2, 3, 7]
[2, 3, 7, 101]
[2, 3, 7, 18]
'''