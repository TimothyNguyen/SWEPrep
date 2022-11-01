class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): 
            return self.findMedianSortedArrays(nums2, nums1)
        
        x, y = len(nums1), len(nums2)
        l, r = 0, x
        while l <= r:
            partitionX = (l + r) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # Do binary search
            maxLeftX = -float('inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            maxLeftY = -float('inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY: r = partitionX - 1
            else: l = partitionX + 1
        return 0.0