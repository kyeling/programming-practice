class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums == null || nums.length == 0) return null; 
        if(nums.length == 1) return new TreeNode(nums[0]);
        if(nums.length == 2) return new TreeNode(nums[0], null, new TreeNode(nums[1]));
        
        int mid = nums.length / 2;
        TreeNode left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, mid));
        TreeNode right = sortedArrayToBST(Arrays.copyOfRange(nums, mid+1, nums.length));
        
        return new TreeNode(nums[mid], left, right);
    }
}
