class Solution(object):
    def removeStones(self, stones):
        def dfs(s1, visited, stones):
            visited.add(s1)
            for s2 in stones:
                if s2 not in visited:
                    if s1[0] == s2[0] or s1[1] == s2[1]:
                        dfs(s2, visited, stones)
        
        temp = []
        for s1 in stones:
            temp.append((s1[0], s1[1]))
        stones = temp
        
        visited = set()
        numIslands = 0
        for s1 in stones:
            #print(s1)
            if s1 not in visited:
                dfs(s1, visited, stones)
                numIslands += 1

        return len(stones) - numIslands