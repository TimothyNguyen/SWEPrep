'''
You are given an m x n matrix maze (0-indexed) with empty cells 
(represented as '.') and walls (represented as '+'). You are also 
given the entrance of the maze, where entrance = [entrancerow, entrancecol] 
denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with 
a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the 
entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance 
does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 
if no such path exists.

Input: maze = [["+","+",".","+"],
               [".",".",".","+"],
               ["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
'''

'''
Approach: BFS - right
    - We search from entrance cell for the nearest boundary cell in all four directions 
      level by level i.e. 0, 1.... until we get boundary
    - Function reached checks if currect cell is boundary and not the entrance cell
Complexity
Time Complexity :- O(m*n)
Space Complexity :- O(m*n)
'''
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance
        m, n, infi = len(maze), len(maze[0]), int(1e5)
        reached = lambda p, q: (not p==x or not q==y) and (p==0 or q==0 or p==m-1 or q==n-1)
        q, ans = deque(), 0
        q.append((x, y, ans))
        directions = [1, 0, -1, 0, 1]
        while q:
            row, col, ans = q.popleft()
            for i in range(4):
                r, c = row + directions[i], col + directions[i + 1]
                if r < 0 or c < 0 or r == m or c == n or maze[r][c] == '+':
                    continue
                if reached(r, c):
                    return ans + 1
                maze[r][c] = '+'
                q.append((r, c, ans + 1))
        return -1
'''
Approach: DFS - wrong
    1. We search from entrance cell for the nearest boundary cell in all four directions and after getting
       the distance from all directions and return the minimum of them
    Time/Spacce: O(m*n)
Problem:
https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/4115
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance
        m, n, infi = len(maze), len(maze[0]), int(1e5)
        reached = lambda p, q: (not p == x or not q == y) and (p==0 or q==0 or p==m-1 or q==n-1)
        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n or maze[i][j] == '+':
                return infi
            if reached(i, j):
                return 0
            maze[i][j] = '+'
            ans = 1+min(dfs(i+1, j), dfs(i-1, j), dfs(i, j+1), dfs(i, j-1))
            maze[i][j] = '.'
            return ans
        ans = dfs(x, y)
        return -1 if ans>=infi else ans
'''

