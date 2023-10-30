import collections
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ## RC ##
        ## APPROACH : BFS ##
        ## EDGE CASE : Like maze I, we just cannot return by checking (i,j) in visited, 
        ## we have to also check the previous distance with which (i,j) is visited and 
        ## what is the current distance. Not only that we have to also check if both 
        ## the distances are equal, we have to check the previous path and curr path values.
        directions = [(1, 0, 'd'),  (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
        queue = collections.deque([(ball[0], ball[1], "", 0)])
        M, N, visited = len(maze), len(maze[0]), {}
        result = collections.defaultdict(list)
        res_length = float('inf')
        while(queue):
            i, j, path, distance = queue.popleft()
            visited[(i,j)] = (path, distance)
            for x, y, d in directions:
                row, col, dist = i, j, distance  
                while 0 <= row + x < M and 0 <= col + y < N and maze[row + x][col + y] == 0:
                    row, col, dist = row + x, col + y, dist + 1
                    if [row, col] == hole:      
                        res_length = min(res_length, dist)
                        result[dist].append(path + d)
                if(row, col) not in visited: 
                    queue.append((row, col, path + d, dist))
                elif visited[(row, col)][1] >= dist and visited[(row, col)][0] > path + d:  # edge case
                        visited[(row, col)] = (path + d, dist)      # make sure to change in visited
                        queue.append((row, col, path + d, dist))    # also need to continue this path even though if its in visited as the current path is better in distance or path.
        return "impossible" if( not result ) else sorted(result[res_length])[0]

class Solution:
    def findShortestWay(self, maze, ball, hole):
        m, n, q, stopped = len(maze), len(maze[0]), [(0, "", ball[0], ball[1])], {(ball[0], ball[1]): [0, ""]}
        while q:
            dist, pattern, x, y = heapq.heappop(q)
            if [x, y] == hole:
                return pattern
            for i, j, p in ((-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                    if [newX, newY] == hole:
                        break
                if (newX, newY) not in stopped or [dist + d, pattern + p] < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, newX, newY))
        return "impossible"