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