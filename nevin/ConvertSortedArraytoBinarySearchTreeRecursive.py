class Solution(object):
    def sortedArrayToBST(self, nums):
        
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0], None, None)
        elif len(nums) == 2:
            return TreeNode(nums[0], None, TreeNode(nums[1], None, None))
        
        mid = int(len(nums) / 2)
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        
        return TreeNode(nums[mid], left, right)
            
            
# divide arrays / subarrays in binary search process:
# find middle index (rounded down bc of division flooring)
# left = root returned by recursive call on left side
# right = root returned by recursive call on right side
