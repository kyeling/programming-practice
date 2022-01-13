class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # even_idxs = [nums[i] for i in range(n) if i % 2 == 0]
        # return sum(even_idxs)
        
        return sum(sorted(nums)[::2])
