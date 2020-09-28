class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        memo = [0]*n
        memo[0] = nums[0]
        for i in range(1, n):
            memo[i] = max(memo[i-1] + nums[i], nums[i])
        return max(memo)
