# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        column_table = []

        def dfs(node, row, column):
            if node is not None:
                columnTable.append((column, row, node.val))
                dfs(node.left, row + 1, column-1)
                dfs(node.right, row + 1, column+1)
        
        # Step 1. Construct the node list, with the coordinates
        dfs(root, 0, 0)

        # step 2. sort nodes
        column_table.sort()

        # Step 3: Retrieve the sorted results grouped by the column index
        ret = list()
        curr_column_index = column_table[0][0]
        curr_column = []
        for column, row, value in column_table:
            if column == curr_column_index:
                curr_column.append(value)
            else:
                # end of a column, and start the next column
                ret.append(curr_column)
                curr_column_index = column
                curr_column = [value]
        # add the last column
        ret.append(curr_column)

        return ret
    
    
