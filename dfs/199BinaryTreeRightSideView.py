def rightSideView(root):

    def dfs(root, res, level):
        if not root: return
        if level > len(res): res.append(root.val)
        dfs(root.right, res, level + 1)
        dfs(root.left, res, level + 1)

    ans = []
    dfs(root, ans, 1)
    return ans