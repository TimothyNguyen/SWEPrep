class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = collections.defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        # create a min-heap on [elapsedTime, city]
        heap = [(0, 1)]

        # chache to record min time per city
        cache = [[] for _ in range(n + 1)]

        while heap:
            dist, city = heapq.heappop(heap)
            if city == n and len(cache[n]) == 2:
                return max(cache[n])
            
            for nei in graph[city]:
                if (dist // change) % 2 == 0:
                    cand = dist + time
                else:
                    cand = math.ceil(dist / (2 * change)) * (2 * change) + time

                if not cache[nei] or (len(cache[nei]) == 1 and cache[nei] != [cand]):
                    cache[nei] += [cand]
                    heapq.heappush(heap, (cand, nei))
        return 0