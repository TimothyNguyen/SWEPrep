from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        visited = set()  # To track fully visited nodes
        visiting = set()  # To track nodes in the current DFS stack

        def dfs(curr_node):
            if curr_node in visiting:  # Cycle detected
                return False
            if curr_node in visited:  # Already fully processed
                return True

            visiting.add(curr_node)
            if curr_node in graph:
                neighbors = graph[curr_node]
                for nei in neighbors:
                    if not dfs(nei):
                        return False
            visiting.remove(curr_node)
            visited.add(curr_node)
            return True

        for node in graph:
            if node not in visited:
                if not dfs(node):
                    return False
        return True