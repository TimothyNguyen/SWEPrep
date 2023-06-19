'''
There is a ball in a maze with empty spaces (represented as 0) and walls 
(represented as 1). The ball can go through the empty spaces by rolling up, 
down, left or right, but it won't stop rolling until hitting a wall. When the 
ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where 
start = [startrow, startcol] and destination = [destinationrow, destinationcol], 
return the shortest distance for the ball to stop at the destination. If the 
ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start 
position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).

Input: maze = [[0,0,1,0,0],
               [0,0,0,0,0],
               [0,0,0,1,0],
               [1,1,0,1,1],
               [0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: -1

Time: O(m * n * log(mn))
Time complexity : O(mn * log(mn)). Complete traversal of maze will 
be done in the worst case giving a factor of mn. Further, poll 
method is a combination of heapifying O(log(n)) and 
removing the top element(O(1)) from the priority queue, and it takes 
O(n) time for n elements. In the current case, poll introduces a 
factor of log(mn).
Space: O(m * n)
'''
import heapq

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        min_heap = [(0, start)]
        dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited = set()
        while min_heap:
            w, [r, c] = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if [r, c] == destination:
                return w
            for x, y in dir:
                dr, dc = r, c
                k = 0
                while 0 <= dr + x < len(maze) and 0 <= dc + y < len(maze[0]) \
                    and maze[dr + x][dc + y] == 0:
                    dr, dc = dr + x, dc + y
                    k += 1
                if(dr, dc) not in visited:
                    heapq.heappush(min_heap, (w + k, [dr, dc]))
        return -1