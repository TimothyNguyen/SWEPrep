class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            if k == len(heap):
                heapq.heappushpop(heap, (dist, x, y))  # O(logK) as time complexity depend on the size of the heap
            else:
                heapq.heappush(heap, (dist, x, y))  # O(logK)
        return [(x, y) for dist, x, y in heap]