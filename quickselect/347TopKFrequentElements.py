class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def partition(l, r, pivot_idx):
            pivot_freq = count[unique[pivot_idx]]

            unique[pivot_idx], unique[r] = unique[r], unique[pivot_idx]

            store_idx = l
            for i in range(l, r):
                if count[unique[i]] < pivot_freq:
                    unique[store_idx], unique[i] = unique[i], unique[store_idx]
                    store_idx += 1
            
            unique[store_idx], unique[r] = unique[r], unique[store_idx]
            return store_idx


        def quickselect(l, r, k_smallest):
            if l == r:
                return
            
            pivot_idx = random.randint(l, r)
            pivot_idx = partition(l, r, pivot_idx)

            if k_smallest == pivot_idx:
                return
            elif k_smallest < pivot_idx:
                quickselect(l, pivot_idx - 1, k_smallest)
            else:
                quickselect(pivot_idx + 1, r, k_smallest)

        count = collections.Counter(nums)
        unique = list(count.keys())
        n = len(unique)
        quickselect(0, n - 1, n - k)
        return unique[(n-k):]
            

