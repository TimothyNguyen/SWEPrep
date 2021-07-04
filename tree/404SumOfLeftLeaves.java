package tree;

public class SumOfLeftLeaves {
     public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public int sumOfLeftLeaves(TreeNode root) {
        if(root == null) return 0;
        return util(root.left, true) + util(root.right, false);
    }
    public int util(TreeNode root, boolean isLeft) {
        if(root == null) return 0;
        if(isLeaf(root) && isLeft) return root.val;
        return util(root.left, true) + util(root.right, false);
    }
    
    public boolean isLeaf(TreeNode node) {
        if(node == null) return false;
        return node.left == null && node.right == null;
    }
}
