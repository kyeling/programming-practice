class Solution {
    public boolean isSymmetric(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();  // only need 1 q, not 2, as long as preserve order
        
        if (root == null) return true;
        q.add(root.left);
        q.add(root.right);
        
        while (!q.isEmpty()) {
            TreeNode node1 = q.poll();
            TreeNode node2 = q.poll();
            if (node1 == null && node2 == null) continue;  // skip iteration of loop to skip enqueueing
            if ((node1 == null || node2 == null) 
                || (node1.val != node2.val)) return false; // forgot this check initially
            
            q.add(node1.left);
            q.add(node2.right);
            q.add(node1.right);
            q.add(node2.left);      
        }
        
        return true;
    }
}
