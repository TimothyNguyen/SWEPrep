class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, start_node, end_node):
        if start_node not in self.edges:
            self.edges[start_node] = []
        if end_node not in self.edges:
            self.edges[end_node] = []
        self.edges[start_node].append(end_node)

    def find_sum(graph):
        sum = 0
        for vertex in graph.edges:
            sum += len(graph.edges[vertex])
        return sum
