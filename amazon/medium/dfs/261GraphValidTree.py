class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        node = None
        for edge in edges:
            if not node:
                node = edge[0]
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        def has_cycle(curr_node, parent_node):
            visited.add(curr_node)

            for nei in graph[curr_node]:
                if nei not in visited:
                    if has_cycle(nei, curr_node):
                        return True
                elif nei != parent_node:
                    return True
            return False

        return (not node and n == 1) or (not has_cycle(node, None) and len(visited) == n)
