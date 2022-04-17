class Graph(object):
    def __init__(self):
        self.edges = dict()
        
    def add_edge(self, u, v):
        self.edges[u].append(v)
        
        
VISITING = 0
DONE_VISITING = 1

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        ans = []
        def has_cycle_helper(vertex, graph, vertex_states):
            if vertex in vertex_states and vertex_states[vertex] == DONE_VISITING: 
                return False
            vertex_states[vertex] = VISITING
            for neighbor in graph.edges[vertex]:
                if neighbor in vertex_states:
                    if vertex_states[neighbor] == VISITING:
                        return True
                    continue
                else:
                    if has_cycle_helper(neighbor, graph, vertex_states): 
                        return True
            vertex_states[vertex] = DONE_VISITING
            ans.append(vertex)
            return False
    
        graph = Graph()
        
        for u in range(numCourses):
            graph.edges[u] = []
        
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph.add_edge(prevCourse, nextCourse)

        vertex_states = dict()
        for vertex in graph.edges:
            if has_cycle_helper(vertex, graph, vertex_states): 
                return []
            
        return ans[::-1]
    
        