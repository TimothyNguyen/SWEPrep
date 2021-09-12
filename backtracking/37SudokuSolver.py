n = 3
N = n * n

rows = [[0] * (N + 1) for _ in range(N)]
cols = [[0] * (N + 1) for _ in range(N)]
boxes = [[0] * (N + 1) for _ in range(N)]

sudokuSolved = False

class Solution:

    def solveSudoku(self, board: List[List[str]]):

        # check if one can place number d in (row, col) cell
        def could_place(d, row, col):
            idx = (row // n) * n + col // n
            return rows[row][d] + cols[col][d] + boxes[idx][d] == 0

        def placeNumber(d, row, col):
            box_idx = (row // n) * n + col // n
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_idx][d] += 1
            board[row][col] = str(d)


        def backtrack(row, col):
            # If cell is empty
            if board[row][col] == '.':
                # Iterate all numbers 1 to 9
                    
        
        for i in range(N):
            for j in range(N):
                num = board[i][j]
                if num != '.':
                    d = int(num)
                    placeNumber(d, i, j)
            
        backtrack(0, 0)
