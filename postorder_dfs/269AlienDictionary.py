class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Create the adjacency list
        adj = { c:set() for w in words for c in w}
        
        # Get each pair
        for i in range(len(words) -1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            # Not a valid ordering
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # Add to our adjacency list
                    adj[w1[j]].add(w2[j])
                    break
            
        visited = dict() # false=visited, True = visited & current path
        res = []
        
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei): return True
            visited[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        return "".join(reversed(res))