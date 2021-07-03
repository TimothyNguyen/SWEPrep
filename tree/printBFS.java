package tree;

import java.util.LinkedList;
import java.util.Queue;

public class printBFS {
    
    class TreeNode {
        int data;
        TreeNode left;
        TreeNode right;
    }

    public void printBFS(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        
        if (root == null)
            return;
        queue.clear();
        queue.add(root);
        while(!queue.isEmpty()){
            TreeNode node = queue.remove();
            System.out.print(node.data + " ");
            if(node.left != null) queue.add(node.left);
            if(node.right != null) queue.add(node.right);
        }
    
    }

}
