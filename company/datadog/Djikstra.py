class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # set distance to infinity for all nodes
        self.distance = float('inf')
        # mark all nodes unvisited
        self.visited = False
        # predecessor
        self.previous = None
    
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight