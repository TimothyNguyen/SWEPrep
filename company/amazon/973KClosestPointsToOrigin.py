class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for p in points:
            heapq.heappush(heap, (p[0]**2 + p[1]**2, p[0], p[1]))
        # heap = heap[:k]
        b = []
        for i in range(k):
            b.append(heapq.heappop(heap))
        ans = []
        for e in b:
            ans.append([e[1], e[2]])
        return ans