class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_k = dict()
        for num in nums:
            if num not in freq_k:
                freq_k[num] = 0
            freq_k[num] += 1
        max_heap = [(-value, key) for key, value in freq_k.items()]
        heapq.heapify(max_heap)
        
        ans = []
        while k > 0:
            v, key = heapq.heappop(max_heap)
            ans.append(key)
            k -= 1
        
        return ans