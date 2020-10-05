class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 1: return n
        memo = [1] * n
        
        for j in range(1, n):
            curr_LIS = 0  # reset longest increasing subseq
            for i in range(j):
                if nums[i] < nums[j]:
                    curr_LIS = max(curr_LIS, memo[i])
            memo[j] = curr_LIS + 1
        
        return max(memo)
