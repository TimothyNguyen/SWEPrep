import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r, pivot_idx):
            pivot = nums[pivot_idx]

            # 1. move pivot to end
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            # 2. move all smaller elements to the left
            store_idx = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1
            
            # 3. move pivot to its final place
            nums[r], nums[store_idx] = nums[store_idx], nums[r]
        
            return store_idx

        def select(l, r, k_smallest):
            if l == r:
                return nums[l]
            
            # select a random pivot_index between 
            pivot_index = random.randint(l, r)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(l, r, pivot_index)

            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(l, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, r, k_smallest)

        return select(0, len(nums) - 1, len(nums) - k)
