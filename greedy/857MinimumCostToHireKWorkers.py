class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        ans = float('inf')

        N = len(quality)
        for captain in range(N):
            # Must pay at least wage[captain] / quality[captain] per qual
            factor = wage[captain] / quality[captain]
            prices = []
            for worker in range(N):
                price = factor * quality[worker]
                if price < wage[worker]: continue
                prices.append(price)
            
            if len(prices) < K: continue
            prices.sort()
            ans = min(ans, sum(prices[:K]))
        return float(ans)
'''
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))
        #print(workers)
        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q
            
            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)
            #print(ans)
            #print(sumq)
        return float(ans)
'''