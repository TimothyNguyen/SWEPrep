'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
Output: 
[["5","3","4","6","7","8","9","1","2"],
 ["6","7","2","1","9","5","3","4","8"],
 ["1","9","8","3","4","2","5","6","7"],
 ["8","5","9","7","6","1","4","2","3"],
 ["4","2","6","8","5","3","7","9","1"],
 ["7","1","3","9","2","4","8","5","6"],
 ["9","6","1","5","3","7","2","8","4"],
 ["2","8","7","4","1","9","6","3","5"],
 ["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Approach
1. Find an empty cell
2. Try a number
3. Check constraints
4. If the number is valid
    - Place it temporarily
    - Call the function recursively to solve the rest of the grid
5. Backtrack
- If it's an invalid solution
    - Reset the cell to empty
    - Try the next number
'''
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_set, col_set, box_set = defaultdict(set), defaultdict(set), defaultdict(set)

        n = len(board)
        
        def is_valid(r, c, num):
            box_idx = (r // 3) * 3 + c // 3
            return num not in row_set[r], num not in col_set[c], num not in box_set[box_idx]
        
        # 1. Load data
        for r in range(n):
            for c in range(n):
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                box_idx = (r // 3) * 3 + (c // 3)
                box_set[box_idx].add(board[r][c])
        
        # 2. Find an empty cell and check if it's valid through backtracking
        def backtrack(r, c):
            # If we get to the end, we're guicci
            if r == n - 1 and c == n:
                return True
            elif c == n:
                c = 0
                r += 1
            
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            box_idx = (r // 3) * 3 + (c // 3)

            # Go through every number from 1 to 10
            for num in range(1, n + 1):
                # If not valid, continue
                if not is_valid(r, c, num):
                    continue
                # Else we put this there and remove after backtrack
                row_set[r].add(num)
                col_set[c].add(num)
                box_set[box_idx].add(num)
                board[r][c] = str(num)

                if backtrack(r, c + 1):
                    return True

                row_set[r].remove(num)
                col_set[c].remove(num)
                box_set[box_idx].remove(num)
                board[r][c] = '.'
            return False

        backtrack(0, 0)

        
        

