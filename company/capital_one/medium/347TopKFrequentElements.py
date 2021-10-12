'''
Given an integer array nums and an integer k, return the k 
most frequent elements. You may return the answer in any order.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_elements = {}
        for num in nums:
            if num not in freq_elements:
                freq_elements[num] = 0
            freq_elements[num] += 1
        max_heap = []
        for key, v in freq_elements.items():
            heapq.heappush(max_heap, (-v, key))
        heapq.heapify(max_heap)
        ans = []
        while k > 0:
            ans.append(heapq.heappop(max_heap)[1])
            k -= 1
        return ans