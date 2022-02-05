MOVE = {
    "U": (-1, 0),
    "L": (0, -1),
    "R": (0, 1),
    "D": (1, 0)
}

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.R, self.C = height, width
        self.head = (0, 0)
        self.body = []
        self.food = food
        
    def move(self, di: str) -> int:
        nr, nc = self.head[0] + MOVE[di][0], self.head[1] + MOVE[di][1]
        
        if 0 <= nr < self.R and 0 <= nc < self.C:
            if (nr, nc) in self.body:
                return -1
            
            self.body.insert(0, (nr, nc))
            if self.food and self.food[0] == [nr, nc]:
                self.food.pop(0)
            else:
                self.body.pop()
            self.head = (nr, nc)
            return len(self.body)
        else:
            return -1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)