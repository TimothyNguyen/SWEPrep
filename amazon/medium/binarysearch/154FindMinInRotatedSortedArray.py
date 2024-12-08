class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m + 1 < len(nums) - 1 and nums[m] > nums[m+1]:
                return nums[m + 1]
            elif m - 1 >= 0 and nums[m-1] > nums[m]:
                return nums[m]
            # Handle duplicates: nums[l] == nums[m] == nums[r]
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            # Left half is sorted
            elif nums[l] <= nums[m]:
                if nums[m] <= nums[r]:  # Entire range sorted
                    return nums[l]
                else:  # Pivot is in the right half
                    l = m + 1
            # Right half is sorted
            else:
                r = m

        # The loop ends when l == r, return the element
        return nums[l]