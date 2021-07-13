class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2: return [i for i in range(n)]
        
        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        # print(neighbors)
    
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
         
        # Initialize the first layer of leaves
        leaves = list()
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        # trim the leaves with bfs
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # Remove the current leaves along with edges
            while leaves:
                leaf = leaves.pop()
                # THe only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # Remove the only edge left
                neighbors[neighbor].remove(leaf)
                # New leaf
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            # Prepare for new leaves
            leaves = new_leaves            
        return leaves