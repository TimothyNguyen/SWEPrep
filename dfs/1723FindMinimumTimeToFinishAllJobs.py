class Solution:
    def minimumTimeRequired(self, A: List[int], k: int) -> int:
        n = len(A)
        A.sort(reverse=True) # opt 1
        self.res = sum(A)
        count = [0] * k

        def dfs(i):
            #print(count)
            if i == n:
                self.res = min(self.res, max(count))
                #print(count)
                #print(self.res)
                return
            for j in range(k):
                if count[j] + A[i] < self.res: # opt 3
                    count[j] += A[i]
                    dfs(i + 1)
                    count[j] -= A[i]
                if count[j] == 0: break # opt 2
            return False
        dfs(0)
        return self.res