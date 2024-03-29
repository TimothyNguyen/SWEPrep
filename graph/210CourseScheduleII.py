class Solution:
    
    UNVISITED, VISITED, SATISFIED = 0, 1, 2
    
    def findOrder(self, numCourses, prerequisites):
        # Keep track of whether or not we see a cycle 
        possible = True
        # child, parent

        graph = defaultdict(list)
        # Convert list of edges to adj map
        for child, parent in prerequisites:
            graph[parent].append(child)
        
        # keep a map of labels to keep track of which node's state is
        state = [Solution.UNVISITED] * numCourses
        order = [] # Topological ordering

        # dfs
        def dfs(root):
            
            # before traversing children, indicate we've visited
            state[root] = Solution.VISITED

            for child in graph[root]:
                # if child unvisited: dfs()
                # else we're in a cycle
                if state[child] == Solution.UNVISITED:
                    isPossible = dfs(child)
                    if not isPossible:
                        return False
                elif state[child] == Solution.VISITED:   
                    return False
                    
            # After traversing children, mark as satisfied and add to ordering
            state[root] = Solution.SATISFIED
            order.insert(0, root)
            return True
            
        # Call dfs on all unvisited nodes\
        for node in range(numCourses):
            if state[node] == Solution.UNVISITED:
                isPossible = dfs(node)
                if not isPossible:
                    return []

        # If possible, return ordering else []
        return order if possible else []

'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for c2, c1 in prerequisites:
            graph[c1].append(c2)

        visited = [False] * numCourses
        finished = set()
        ans = []

        def dfs(courseNum):
            if visited[courseNum]:
                return visited[courseNum]
            visited[courseNum] = True
            for next_course in graph[courseNum]:
                if next_course not in finished:
                    if visited[next_course] == False:
                        if dfs(next_course):
                            return True
                    else:
                        return True
            finished.add(courseNum)
            ans.append(courseNum)
            return False

        for courseNum in range(numCourses):
            if visited[courseNum] == False and courseNum not in finished:
                if dfs(courseNum):
                    return []
        return ans[::-1]
'''

        