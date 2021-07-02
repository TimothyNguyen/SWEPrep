package tree;

public class printOrder {
    class TreeNode {
        int data;
        TreeNode left;
        TreeNode right;
    }

    void printPreorder(TreeNode node) {	
        if (node == null) return;
        System.out.print(node.data + " "); // process node
        printPreorder(node.left); // recurse on left
        printPreorder(node.right); // recrse on right
    }

    void printPostorder(TreeNode node) {
        if (node == null) return;
        printPostorder(node.left); // recurse on left
        printPostorder(node.right); // recurse on right
        System.out.println(node.data + " "); // process node
    }
    
    void printInorder(TreeNode node) {
        if (node == null) return;
        printInorder(node.left); // process left
        System.out.println(node.data); // process node
        printInorder(node.right); // process right
    }

}
