/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serialHelp(root, sb);
        return sb.toString();
    }

    // Creates the string in preorder traversal with marker for Null pointers
    public void serialHelp(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append("NULL,");
        }
        else {
            sb.append(root.val).append(",");
            serialHelp(root.left, sb);
            serialHelp(root.right,sb);
        }
    }
    
    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Queue<String> nodes = new LinkedList<>();
        nodes.addAll(Arrays.asList(data.split(",")));
        return buildTree(nodes);
    }
    
    // Build the tree by going through preorder traversal
    public TreeNode buildTree(Queue<String> nodes) {
        String val = nodes.remove();
        if (val.equals("NULL")) return null;
        else {
            TreeNode node = new TreeNode(Integer.valueOf(val));
            node.left = buildTree(nodes);
            node.right = buildTree(nodes);
            return node;
        }
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));