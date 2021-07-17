
class Graph(object):
    def __init__(self):
        self.edges = dict()
    
    def add_edge(self, u, v):
        self.edges[u].append(v)
class Solution(object):

    UNVISITED, VISITED = 0, 1

    def finishAllTasks(self, task_list):
        # First construct the graph.
        graph = Graph()
        for task in task_list:
            if task[1] not in graph:
                graph[task[1]] = []
            graph[task[1]].append(task[0])
        
        def has_no_cycle(course, course_states):
            # If it's already visited, you've found a cycle and rip
            if course in course_states and course_states[course] == Solution.VISITED:
                return False
            # Mark the course as visited now
            course_states[course] = Solution.UNVISITED
            # Else, find all the neighboring nodes 
            for nei in graph[course]:
                if nei in course_states:
                    if course_states[nei] == Solution.UNVISITED:
                        return False
                    elif course_states[nei] == Solution.VISITED:
                        continue
                else:
                    if has_no_cycle(nei):
                        return False
            course_states[course] = Solution.VISITED
            return True
        
        # Go through the graph, created
        course_states = dict()
        for node in graph.edges:
            # do a dfs to see if there's a cycle. If yes, return false
            if not has_no_cycle(node, course_states): return False
        # Return true
        return True
