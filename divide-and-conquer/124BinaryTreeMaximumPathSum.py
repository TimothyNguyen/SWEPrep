class Solution {
    private int max = Integer.MAX_VALUE;
    public int maxPathSum(TreeNode root) {
        if(root == null) return 0;
        dfs(root, 0);
        return max;
    }

    private int dfs(TreeNode root, int value) {
        if(root == null) return 0;
        int left = dfs(root.left, value);
        int right = dfs(root.right, value);
        int currMax = Math.max(left + right + root.val, Math.max(left + root.val, Math.max(right + root.val, root.val)));
        if(max < currMax) max = currMax;
        return Math.max(right + root.val, Math.max(left + root.val, root.val));        
    }
}