'''
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing 
the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no 
adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] 
represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change 
it to a revealed blank 'B' and all of its adjacent unrevealed squares 
should be revealed recursively.

If an empty square 'E' with at least one adjacent mine is revealed, 
then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed
'''

from collections import deque

class Solution:
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        clickY, clickX = click
        if board[clickY][clickX] == 'M':
            board[clickY][clickX] = 'X'
            return board
        stack = deque([(clickY, clickX)])
        visited = set((clickY, clickX))
        while len(stack) > 0:
            y, x = stack.pop()
            numAdjacentMines = self.getNumAdjacentMines(y, x, board)
            board[y][x] = 'B' if numAdjacentMines == 0 else str(numAdjacentMines)
            if numAdjacentMines > 0:
                continue
            for direction in Solution.directions:
                newY, newX = direction[0] + y, direction[1] + x
                if not self.isWithinBounds(newY, newX, board):
                    continue
                elif board[newY][newX] == 'E' and (newY, newX) not in visited:
                    stack.append((newY, newX))
                    visited.add((newY, newX))
        return board
            
    def getNumAdjacentMines(self, y, x, board):
        numAdjacentMines = 0
        for direction in Solution.directions:
            newY, newX = direction[0] + y, direction[1] + x
            if not self.isWithinBounds(newY, newX, board):
                continue
            elif board[newY][newX] == 'M':
                numAdjacentMines += 1
        return numAdjacentMines
    
    def isWithinBounds(self, y, x, board):
        height, width = len(board), len(board[0])
        return 0 <= y < height and 0 <= x < width