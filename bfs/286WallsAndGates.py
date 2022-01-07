'''
You are given an m x n grid rooms initialized with these three 
possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 
to represent INF as you may assume that the distance to a gate is less 
than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is 
impossible to reach a gate, it should be filled with INF.
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        arr=[(i,j) for i in range(len(rooms)) for j in range(len(rooms[0])) if rooms[i][j]==0]
        while arr:
            new=[]
            for i,j in arr:
                possible=[(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0<=x<len(rooms) and 0<=y<len(rooms[0]) and rooms[x][y]==2**31-1]
                for x,y in possible:
                    rooms[x][y]=rooms[i][j]+1
                    new.append((x,y))
            arr=new