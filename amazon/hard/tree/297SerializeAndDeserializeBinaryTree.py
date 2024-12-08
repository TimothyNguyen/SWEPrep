# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = []
        def preorder(node):
          if not node:
            s.append('n')
            return
          s.append(str(node.val))
          preorder(node.left)
          preorder(node.right)
        preorder(root)
        # print(s)
        return ' '.join(s)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue = collections.deque(data.split())
        def preorder():
          s = queue.popleft()
          if s == 'n':
            return None
          node = TreeNode(s)
          node.left = preorder()
          node.right = preorder()
          return node
        return preorder()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))