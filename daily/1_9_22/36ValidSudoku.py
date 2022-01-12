'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled 
cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain 
the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not 
necessarily solvable. Only the filled cells need to be 
validated according to the mentioned rules.

Time/Space: O(N^2)
'''

class Solution:
    def isValidSudoku(self,  board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if board[r][c] in rows[r]:
                        return False
                    rows[r].add(board[r][c])

                    if board[r][c] in cols[c]:
                        return False
                    cols[c].add(board[r][c])

                    box_idx = (r // 3) * 3 + c // 3
                    if board[r][c] in boxes[box_idx]:
                        return False
                    boxes[box_idx].add(board[r][c])
        return True