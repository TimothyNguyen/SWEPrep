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
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        def has_cycle_helper(vertex, graph, vertex_states):
            if vertex in vertex_states and vertex_states[vertex] == DONE_VISITING:
                return False
            vertex_states[vertex] = VISITING
            for neighbor in graph.edges[vertex]:
                if neighbor in vertex_states:
                    if vertex_states[neighbor] == VISITING:
                        return True
                    elif vertex_states[neighbor] == DONE_VISITING:
                        continue
                else:
                    if has_cycle_helper(neighbor, graph, vertex_states):
                        return True
            vertex_states[vertex] = DONE_VISITING
            return False
    
        graph = Graph()
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph.add_edge(prevCourse, nextCourse)

        vertex_states = dict()
        for vertex in graph.edges:
            if has_cycle_helper(vertex, graph, vertex_states): 
                return False
        return True
    