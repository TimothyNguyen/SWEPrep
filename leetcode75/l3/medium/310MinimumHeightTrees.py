'''
A tree is an undirected graph in which any two vertices are connected by exactly 
one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 
edges where edges[i] = [ai, bi] indicates that there is an undirected 
edge between the two nodes ai and bi in the tree, you can choose any node of the tree 
as the root. When you select a node x as the root, the result tree has height h. 
Among all possible rooted trees, those with minimum height (i.e. min(h))  
are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path 
between the root and a leaf.

Let |V| be the number of nodes in the graph
Time/Space: O(|V|)
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        # build the graph with adj list
        neighbors = [set() for i in range(n)]

        for start, end in neighbors:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        # Trim the leaves with bfs
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                # The neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # Remove the only edge left
                neighbors[neighbor].remove(leaf)
                # new leaf
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            # Prep for new_leaves
            leaves = new_leaves
        return leaves