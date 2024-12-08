from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        visited = set()  # To track fully visited nodes
        visiting = set()  # To track nodes in the current DFS stack

        def has_cycle(curr_node):
            if curr_node in visiting:  # Cycle detected
                return True
            if curr_node in visited:  # Already fully processed
                return False

            visiting.add(curr_node)
            if curr_node in graph:
                neighbors = graph[curr_node]
                for nei in neighbors:
                    if has_cycle(nei):
                        return True
            visiting.remove(curr_node)
            visited.add(curr_node)
            return False

        for node in graph:
            if node not in visited:
                if has_cycle(node):
                    return True
        return False