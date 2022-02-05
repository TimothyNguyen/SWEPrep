class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        todo = False
        for r in range(R):
            for c in range(C - 2):
                val = abs(board[r][c])
                if val != 0 and abs(board[r][c+1]) == abs(board[r][c+2]) == val:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -val
                    todo = True
        for r in range(R-2):
            for c in range(C):
                val = abs(board[r][c])
                if val != 0 and abs(board[r+1][c]) == abs(board[r+2][c]) == val:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -val
                    todo = True
        
        # Now crush
        # Stat at bottom left and move up
        for c in range(C):
            wr = R - 1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
                
        return self.candyCrush(board) if todo else board