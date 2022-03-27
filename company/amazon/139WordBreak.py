class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue, visited = [0],  len(s) * [0]
        hashset = set(wordDict)
        while queue:
            start = queue.pop(0)
            if visited[start] == 0:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in hashset:
                        queue.append(end)
                        if end == len(s): return True
                visited[start] = 1
        return False