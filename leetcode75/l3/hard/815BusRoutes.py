'''
You are given an array routes representing bus routes where routes[i] is a bus route 
that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the 
sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you 
want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. 
Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then 
take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1


'''
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                to_routes[j].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T: return bus
            for i in to_routes[stop]:
                for j in routes[i]:
                    if j not in seen:
                        bfs.append((j, bus + 1))
                        seen.add(j)
                routes[i] = []  # seen route
        return -1
        '''
        if source == target:
            return 0
        graph = defaultdict(set)
        
        def intersect(arr1, arr2):
            l, r = 0, 0
            while l < len(arr1) and r < len(arr2):
                if arr1[l] == arr2[r]:
                    return True
                if arr1[l] < arr2[r]:
                    l += 1
                else:
                    r += 1
            return False
        
        # Build the graph
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if intersect(routes[i], routes[j]):
                    graph[i].add(j)
                    graph[j].add(i)
        seen, targets = set(), set()
        routes_set = map(set, routes)
        for node, route in enumerate(routes_set):
            if source in route:
                seen.add(node)
            if target in route:
                targets.add(node)
        
        queue = deque((node, 1) for node in seen)
        while queue:
            node, depth = queue.popleft()
            if node in targets:
                return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1  
        '''