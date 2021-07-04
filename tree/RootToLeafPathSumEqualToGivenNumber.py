def pathSum(root):
    ans = []
    def dfs(root, value):
        if root == None: return 0
        if not root.left and not root.right: 
            ans.append(root.val + value)
            return
        if root.left: dfs(root.left, root.val + value)
        if root.right: dfs(root.right, root.val + value)
    dfs(root, 0)
    return ans