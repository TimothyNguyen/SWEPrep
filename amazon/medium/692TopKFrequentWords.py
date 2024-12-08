class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = defaultdict(int)
        for word in words:
            word_dict[word] += 1
        min_heap = []
        for word, v in word_dict.items():
            heapq.heappush(min_heap, (-v, word))
        ans = []
        while k > 0:
            v, word = heapq.heappop(min_heap)
            ans.append(word)
            k -= 1
        return ans