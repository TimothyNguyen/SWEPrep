'''
There is a ball in a maze with empty spaces (represented as 0) 
and walls (represented as 1). The ball can go through the 
empty spaces by rolling up, down, left or right, but it
won't stop rolling until hitting a wall. When the ball 
stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the
destination, where start = [startrow, startcol] and 
destination = [destinationrow, destinationcol], return 
true if the ball can stop at the destination, otherwise 
return false.

You may assume that the borders of the maze are all 
walls (see examples).

Input: maze = [[0,0,1,0,0],
               [0,0,0,0,0],
               [0,0,0,1,0],
               [1,1,0,1,1],
               [0,0,0,0,0]], 
start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Time/Space: O(mn)
'''

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
         
        def dfs(maze: List[List[int]], start: List[int], destination: List[int], visited) -> bool:
            x, y = start[0], start[1]
            if visited[x][y] == True:
                return False
            if start == destination:
                return True

            visited[x][y] = True
            left, right, up, down = y-1, y+1, x-1, x+1
            
            # left
            while left >= 0 and maze[x][left] == 0:
                left -= 1
            if dfs(maze, (x, left + 1), destination, visited):
                return True
            
            # right
            while right < len(maze[0]) and maze[x][right] == 0:
                right += 1
            if dfs(maze, (x, right-1), destination, visited):
                return True
            
            # up
            while up >= 0 and maze[up][y] == 0:
                up -= 1
            if dfs(maze, (up+1, y), destination, visited):
                return True
            
            # down
            while down < len(maze) and maze[down][y] == 0:
                down += 1
            if dfs(maze, (down-1, y), destination, visited):
                return True
            
            return False
        
            
        
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]
        return dfs(maze, (start[0], start[1]), (destination[0], destination[1]), visited)
        