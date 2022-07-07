class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # on each iteration, keep track of min seen so far,
        # compute current element - min, and update max difference 
        temp_min = nums[0]
        max_diff = 0
        for num in nums[1:]:
            max_diff = max(max_diff, num - temp_min)
            temp_min = min(temp_min, num)
        
        # return max difference or -1 if difference is non positive
        return -1 if not max_diff else max_diff
