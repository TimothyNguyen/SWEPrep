class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def add_node(self, node):
        if not self.root:
            self.root = node
            return None
        
        def insert(root, node):
            if root.val < node.val:
                if root.left: insert(root.left, node)
                else: root.left = node
            else:
                if root.right: insert(root.right, node)
                else: root.right = node
        insert(self.root, node)
    
    def traverse(self):
        if self.root is None: return None

        def dfs(node):
            print("preorder", node.val)
            if node.left: dfs(node.left)
            print("inorder", node.val)
            if node.right: dfs(node.right)
            print("postorder", node.val)
        dfs(self.root)
    
    def bfs(self):
        if self.root is None: return None
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    