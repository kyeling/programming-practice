class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0] * (target + 1)
        
        for i in range(1, target + 1):
            for denom in nums:
                if denom == i:
                    memo[i] += 1
                if i > denom:
                    memo[i] += memo[i - denom]
        
        return memo[-1]
