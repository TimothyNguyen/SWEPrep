class Graph(object):
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, start_node, end_node):
        if start_node not in self.edges:
            self.edges[start_node] = []
        if end_node not in self.edges:
            self.edges[end_node] = []
        self.edges[start_node].append(end_node)
        
VISITING = 0
DONE_VISITING = 1
class Solution(object):        
    def eventualSafeNodes(self, g):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        
        not_safe = set()
        def has_cycle_helper(vertex, graph, vertex_states):
            if vertex in vertex_states and vertex_states[vertex] == DONE_VISITING:
                return False
            vertex_states[vertex] = VISITING
            for neighbor in graph.edges[vertex]:
                if neighbor in vertex_states:
                    if vertex_states[neighbor] == VISITING:
                        not_safe.add(neighbor)
                        return True
                    elif vertex_states[neighbor] == DONE_VISITING:
                        continue
                else:
                    if has_cycle_helper(neighbor, graph, vertex_states):
                        not_safe.add(neighbor)
                        return True
            vertex_states[vertex] = DONE_VISITING
            return False
    
        graph = Graph()
        for i in range(len(g)):
            for node in g[i]:
                graph.add_edge(i, node)

        vertex_states = dict()
        for vertex in graph.edges:
            if has_cycle_helper(vertex, graph, vertex_states):
                not_safe.add(vertex)
        
        ans = []
        for i in range(len(g)):
            if i not in not_safe: 
                ans.append(i)
        
        return ans