class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        n = len(arr)
        max_from_left, min_from_right = [0] * len(arr), [0] * len(arr)
        max_from_left[0], min_from_right[-1] = arr[0], arr[-1]

        
        for i in range(1, n):
            max_from_left[i] = max(max_from_left[i - 1], arr[i])
            min_from_right[n - i - 1] = min(min_from_right[n - i], arr[n - i - 1])

            
        ans = 1
        # If max of left <= min of right
        for i in range(n - 1):
            if max_from_left[i] <= min_from_right[i + 1]:
                ans += 1
        return ans