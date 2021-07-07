class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, start_node, end_node):
        if start_node not in self.edges:
            self.edges[start_node] = []
        if end_node not in self.edges:
            self.edges[end_node] = []
        self.edges[start_node].append(end_node)


VISITING = 0
DONE_VISITING = 1

def has_cycle(graph):
    vertex_states = dict()
    for vertex in graph.edges:
        if has_cycle_helper(vertex, graph, vertex_states):
            return True
        return False


def has_cycle_helper(vertex, graph, vertex_states):
    if vertex in vertex_states and vertex_states[vertex] == DONE_VISITING:
        return False
    vertex_states[vertex] = VISITING
    for neighbor in graph.edges[vertex]:
        if neighbor in vertex_states:
            if vertex_states[neighbor] == VISITING:
                return True
            elif vertex_states[neighbor] == DONE_VISITING:
                continue
        else:
            if has_cycle_helper(neighbor, graph, vertex_states):
                return True
    vertex_states[vertex] = DONE_VISITING
    return False
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(1, 3)
graph.add_edge(4, 2)
graph.add_edge(5, 2)
print(graph.edges)