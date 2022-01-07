class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n] * n
        self.row_map, self.col_map = dict(), dict()
        self.d1_map, self.d2_map = dict(), dict()
        self.n = n
        
    def move(self, row: int, col: int, player: int) -> int:
        # if board[row][col] != 0: - assume using all valid moves
        self.board[row][col] = player
        #num_moves += 1
        
        # Rows
        if row not in self.row_map:
            self.row_map[row] = {}
        if player not in self.row_map[row]:
            self.row_map[row][player] = 0
        self.row_map[row][player] += 1
        if self.row_map[row][player] == self.n:
            return player
        
        # Cols
        if col not in self.col_map:
            self.col_map[col] = {}
        if player not in self.col_map[col]:
            self.col_map[col][player] = 0
        self.col_map[col][player] += 1
        if self.col_map[col][player] == self.n:
            return player
        
        # Special diagonal cases
        if row == col:
            if player not in self.d1_map:
                self.d1_map[player] = 0
            self.d1_map[player] += 1
            if self.d1_map[player] == self.n:
                return player
        
        if row + col + 1 == self.n:
            if player not in self.d2_map:
                self.d2_map[player] = 0
            self.d2_map[player] += 1
            if self.d2_map[player] == self.n:
                return player
        
        return 0
    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)