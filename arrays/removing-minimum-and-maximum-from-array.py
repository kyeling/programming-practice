class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        first = min(min_idx, max_idx)
        second = max(min_idx, max_idx)
        return min(first + 1 + n - second, 
                   second + 1, 
                   n - first)
    
    # 3 cases
    # front and back: min(min_idx, max_idx) + 1 + len(nums) - max(min_idx, max_idx)
    # both front: max(min_idx, max_idx) + 1
    # both back: len(nums) - min(min_idx, max_idx)
    
    # [2,10,7,5,4,1,8,6]
    #  0 1  2 3 4 5 6 7, len = 8
    
    # edge case: 1 element array
    
    # time complexity: O(n) for first and second min, total runtime O(n)
    # space complexity: O(1) for four variables
