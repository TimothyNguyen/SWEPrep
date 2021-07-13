from collections import defaultdict, deque

class GNode(object):
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(GNode)
        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1
        
        
        # We start from courses that have no prereqs.
        stack = deque()
        for course_num, node in graph.items():
            if node.inDegrees == 0:
                stack.append(course_num)
        
        removedEdges = 0
        while stack:
            course_num = stack.pop()
        
            # Remove edges 1 by 1
            for nextCourse in graph[course_num].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
                
                # while removing edges, we might discover new 
                # courses with prerequisites removed, i.e. new 
                # courses without prerequisites.
                if graph[nextCourse].inDegrees == 0:
                    stack.append(nextCourse)
                
        if removedEdges == totalDeps: 
            return True
        else:
            # if there are still some edges left, then there exist some cycles
            # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
            return False