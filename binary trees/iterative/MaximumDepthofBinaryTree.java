class Solution {
    public int maxDepth(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        int levels = 0;
        int numNodes = 0;
        TreeNode curr = null;
        
        if(root != null) q.add(root);
        while(!q.isEmpty()){
            // store length of queue (number of nodes in level)
            numNodes = q.size();
            
            // pop until length = 0, enqueueing children if exist
            while(numNodes != 0) {
                curr = q.poll();
                if(curr.left != null) q.add(curr.left);
                if(curr.right != null) q.add(curr.right);
                numNodes--;                
            }
            // add 1 to level (loop ends when no children enqueued)
            levels++;
        }
        return levels;
    }
}

/** 
iterative approach:
- if a level of children exists, add 1 (root node is height 0 bc no edges)
- pop every node at level and enqueue children
- to tell when queue has cycled through a level, store size of queue and pop until --size == 0
**/
