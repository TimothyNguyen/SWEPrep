'''
There are n couples sitting in 2n seats arranged in a row and want to hold hands.

The people and seats are represented by an integer array row where row[i] is the ID of 
the person sitting in the ith seat. The couples are numbered in order, the first couple 
being (0, 1), the second couple being (2, 3), and so on with the last couple being 
(2n - 2, 2n - 1).

Return the minimum number of swaps so that every couple is sitting side by side. A swap 
consists of choosing any two people, then they stand up and switch seats.

Example 1:

Input: row = [0,2,1,3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:

Input: row = [3,2,0,1]
Output: 0
Explanation: All couples are already seated side by side.

Approach: This graph is 2-regular (every node has degree 2), and it is easy to see that every 
connected component of this graph must be a cycle. Then, making a swap for X1 to meet their 
partner X2 has a corresponding move on the couples graph equivalent to contracting the 
corresponding edge to X1X2 plus having anode with a single self edge. Our goal is to have N
connected components in the graph, one for each couch. Every swap, (allowed by the scheme above)
always increases that number by exactly 1, so under HSA, the answer is just N minus the 
number of connected components in the couples graph.

Now, to prove HSA, observe that is impossible with any swap to create more than 1 additional
connected component in the couples graph. So any optimal solution must have at least the number
of moves in the answer we've constructed.

We'll construct the graph: adj[node] will be the index of the two nodes that this node 
is adjacent to. After, we'll find all connected components (which are also cycles.) If 
at some couch (node) a person is unvisited, we will visit it and repeatedly visit 
some neighbor until we complete the cycle.

Time: O(N), where N is the number of couples
Space Complexity: O(N), the size of adj and associated data structures.
'''

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        
        # couples[x] = [i, j]. x-th couple is at couches i and j
        couples = [[] for _ in range(n)]
        for i, x in enumerate(row):
            couples[x // 2].append(i // 2)
        # print(couples)
        # adj[x] = [i, j]
        # x-th couch connected to couches i, j by couples
        adj = [[] for _ in range(n)]
        for x, y in couples:
            adj[x].append(y)
            adj[y].append(x)
        # print(adj)
        
        # Answer is N minus the number of cycles in "adj"
        ans = n
        for start in range(n):
            if not adj[start]:
                continue
            ans -= 1
            x, y = start, adj[start].pop()
            while y != start:
                adj[y].remove(x)
                x, y = y, adj[y].pop()
        
        return ans