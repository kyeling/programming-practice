class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        maxes=[0]*n
        mins=[0]*n
        maxes[0]=mins[0]=nums[0]
        
        for i in range(1,n):
            num = nums[i]
            maxes[i]=max(num, maxes[i-1] * num, mins[i-1] * num)
            mins[i]=min(num, maxes[i-1] * num, mins[i-1] * num)
        return max(maxes)
