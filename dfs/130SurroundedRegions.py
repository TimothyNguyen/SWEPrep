class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])
        border_cells = set()
        
        def dfs(r, c):
            if board[r][c] != 'O': return
            board[r][c] = 'E'
            if c < n - 1: dfs(r, c+1)
            if c > 0: dfs(r, c-1)
            if r < m - 1: dfs(r + 1, c)
            if r > 0: dfs(r - 1, c)
                
        # Capture all border cells and mark it as an 'E' if it's an 'O'
        for c in range(n): 
            if board[0][c] == 'O': border_cells.add((0, c))
            if board[m-1][c] == 'O': border_cells.add((m-1, c))
        for r in range(m): 
            if board[r][0] == 'O': border_cells.add((r, 0))
            if board[r][n-1] == 'O': border_cells.add((r, n-1))
        
        # mark escaped 'O'
        #print(border_cells)
        for x, y in border_cells:
            dfs(x, y)
        
        
        # Go through the other cells in the board
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E': 
                    board[r][c] = 'O'  # escaped
        return board