class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set({})
        if n == 0 or n == 1: return False
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
