class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n = len(nums1) + len(nums2)
        partition_len = n // 2
        l, r = 0, len(nums1) - 1

        # Look at the smaller array
        while True:
            m1 = (l + r) // 2
            m2 = partition_len - (m1 + 2)
            l1 = nums1[m1] if m1 >= 0 else float('-inf')
            r1 = nums1[m1 + 1] if m1 + 1 < len(nums1) else float('inf')
            l2 = nums2[m2] if m2 >= 0 else float('-inf')
            r2 = nums2[m2 + 1] if m2 + 1 < len(nums2) else float('inf')

            # If the partition is good, we can find the median
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)
            elif l2 > r1:
                l = m1 + 1
            else:
                r = m1 - 1
        return -1
