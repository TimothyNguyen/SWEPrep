'''
This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where 
board[i][j] represents the type of candy. A value of board[i][j] == 0 
represents that the cell is empty.

The given board represents the state of the game following the player's 
move. Now, you need to restore the board to a stable state by crushing 
candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the stable board.
'''

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Ad-hoc (Crush and Gravity)
        R, C = len(board), len(board[0])
        todo = False
        
        # Do for horizontal
        for r in range(R):
            for c in range(C - 2):
                v = abs(board[r][c])
                if v != 0 and v == abs(board[r][c + 1]) and v == abs(board[r][c+2]):
                    board[r][c] = board[r][c+1] = board[r][c+2] = -v
                    todo = True
            
        # Do for vertical
        for r in range(R - 2):
            for c in range(C):
                v = abs(board[r][c])
                if v != 0 and v == abs(board[r + 1][c]) and v == abs(board[r + 2][c]):
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -v
                    todo = True
        
        # Now crush
        for c in range(C):
            wr = R - 1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
        
        return self.candyCrush(board) if todo else board