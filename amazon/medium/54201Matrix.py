class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        seen = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    seen.add((i, j))
                    queue.append((i, j))
        
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        level = 1
        while queue:
            l = len(queue)
            idx = 0
            while idx < l:
                x, y = queue.popleft()
                for dir in dirs:
                    new_x, new_y = x + dir[0], y + dir[1]
                    if 0 <= new_x < len(mat) and 0 <= new_y < len(mat[0]) and (new_x, new_y) not in seen and mat[new_x][new_y] == 1:
                        mat[new_x][new_y] = level
                        queue.append((new_x, new_y))
                        seen.add((new_x, new_y))
                idx += 1
            level += 1
        return mat
                    
                
            