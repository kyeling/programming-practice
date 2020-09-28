class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            addend = target - num
            if addend in seen:
                return [seen[addend], i]
            seen[num] = i
        return ["i love acm"]

# efficient access to prev elements (compared to other method with nested for loop)
