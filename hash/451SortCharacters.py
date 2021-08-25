class Solution:
    def frequencySort(self, s: str) -> str:
        freq_words = dict()
        for ch in s:
            if ch not in freq_words:
                freq_words[ch] = 0
            freq_words[ch] += 1
        max_heap = [(-value, key) for key, value in freq_words.items()]
        heapq.heapify(max_heap)
        
        ans = []
        while max_heap:
            v, k = heapq.heappop(max_heap)
            ans += [k] * -v
        return ''.join(ans)