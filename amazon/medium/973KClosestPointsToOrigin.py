import heapq

class Solution(object):
    def kClosest(self, points, K):
        heap = []
        ans = []
        for x, y in points:
            if len(heap) < K:
                heapq.heappush(heap, (-(x ** 2 + y ** 2), [x, y]))
            else:
                heapq.heappushpop(heap, (-(x ** 2 + y ** 2), [x, y]))
        while len(heap) > 0:
            _, arr = heapq.heappop(heap)
            ans.append(arr)
        return ans
        # points.sort(key = lambda P: P[0]**2 + P[1]**2)
        # return points[:K]
'''
Time: O(n log K)
Space: O(K) - will store at most K points at any time
'''