class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = dict()
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[stack[-1]] <= nums2[i]:
                stack.pop()
            res[nums2[i]] = nums2[stack[-1]] if stack else -1
            stack.append(i)
        
        for i in range(len(nums1)):
            nums1[i] = res[nums1[i]]
        
        return nums1