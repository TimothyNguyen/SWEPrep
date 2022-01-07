'''
There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid 
square are (x, y).

We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. 
There is also an array of blocked squares, where each blocked[i] = [xi, yi] represents a 
blocked square with coordinates (xi, yi).

Each move, we can walk one square north, east, south, or west if the square is not in 
the array of blocked squares. We are also not allowed to walk outside of the grid.

Return true if and only if it is possible to reach the target square from the source
square through a sequence of valid moves.

Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: The target square is inaccessible starting from the source square because we cannot move.
We cannot move north or east because those squares are blocked.
We cannot move south or west because we cannot go outside of the grid.
Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: Because there are no blocked cells, it is possible to reach the target square.

Additional Questions: 
Question: What is the maximum area?
Answer
It maximum blocked is achieved when the blocked squares,
surrounding one of the corners as a 45-degree straight line.

And it's easily proved.

If two cells are connected horizontally,
we can slide one part vertically to get bigger area.

If two cells are connected vertically,
we can slide one part horizontally to get bigger area.


Question: Can we apply a BFS?
Answer
Yes, it works.
BFS in 4 directions need block.length * 2 as step bounds,
BFS in 8 directions need block.length as step bounds.

It needs to be noticed that,
The top voted BFS solution is WRONG with bound,
though it's accpected by Leetcode.

But compared with the complexity:
Searching with limited area is O(0.5B*B).
BFS with steps can be O(2B^B).

Intution: Simple search will get TLE, because the big search space. Anyway,
we don't need to go further to know if we are blocked or not.
Because the maximum area blocked are 19900.

Explanation:
Search from source -> target,
if find, return true;
if not find, return false;
if reach 20000 steps, return true.

Then we do the same thing searching from target to source

Complexity:
Time complexity depends on the size of blocked
The maximum area blocked are B * (B - 1) / 2
As a result, time and space complexity are both O(B^2)
In my solution I used a fixed upper bound 20000.
'''
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(map(tuple, blocked))
        # print(blocked)
        
        def dfs(x, y, target, seen):
            if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in seen: 
                return False
            seen.add((x, y))
            if len(seen) > 20000 or [x, y] == target: 
                return True
            return dfs(x + 1, y, target, seen) or \
                dfs(x - 1, y, target, seen) or \
                dfs(x, y - 1, target, seen) or \
                dfs(x, y + 1, target, seen)
            
        return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())
        
        '''
        blocked = {tuple(p) for p in blocked}

        def bfs(source, target):
            bfs, seen = [source], {tuple(source)}
            for x0, y0 in bfs:
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target: return True
                        bfs.append([x, y])
                        seen.add((x, y))
                if len(bfs) == 20000: return True
            return False
        return bfs(source, target) and bfs(target, source)
        '''
        
        
'''
class Solution {
    static int dirs[][] = new int[][]{{0,1}, {1,0}, {-1,0}, {0,-1}};
    static int limit = (int)1e6;
    public boolean isEscapePossible(int[][] blocked, int[] source, int[] target) {
        Set<String> blocks = new HashSet<>();
        for(int block[] : blocked)
            blocks.add(block[0] + ":" + block[1]);
        return bfs(source, target, blocks) && bfs(target, source, blocks);
    }
    public boolean bfs(int[] source, int[] target, Set<String> blocks){
        Set<String> seen = new HashSet<>();
        seen.add(source[0] + ":" + source[1]);
        Queue<int[]> bfs = new LinkedList<>();
        bfs.offer(source);
        
        while(!bfs.isEmpty()){
            int cur[] = bfs.poll();
            for(int dir[] : dirs){
                int nextX = cur[0] + dir[0];
                int nextY = cur[1] + dir[1];
                if(nextX < 0 || nextY < 0 || nextX >= limit || nextY >= limit) continue;
                String key = nextX + ":" + nextY;
                if(seen.contains(key) || blocks.contains(key)) continue;
                if(nextX == target[0] && nextY == target[1]) return true;
                bfs.offer(new int[]{nextX, nextY});
                seen.add(key);
            }
            if(seen.size() == 20000) return true;
        }
        return false;
    }
}
'''