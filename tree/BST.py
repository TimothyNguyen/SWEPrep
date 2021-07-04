class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def add_node(self, node):
        if not self.root:
            self.root = node
            return None
        
        def insert(root, node):
            if root.val < node.data:
                if root.left: insert(root.left, node)
                else: root.left = node
            else:
                if root.right: insert(root.right, node)
                else: root.right = node
        insert(self.root, node)