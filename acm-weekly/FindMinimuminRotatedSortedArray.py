class Solution(object):
    def findMin(self, nums):
        leftIdx = 0
        rightIdx = len(nums) - 1
        
        while leftIdx < rightIdx:
            midIdx = leftIdx + (rightIdx - leftIdx) / 2
            
            if nums[midIdx] <= nums[rightIdx]:
                rightIdx = midIdx
            else:
                leftIdx = midIdx + 1
        
        return nums[leftIdx]

# cases
#   middle greater than rightIdx (min on right)
#   middle smaller than rightIdx, it is smallest 
#   middle smaller than rightIdx, but not smallest
# notes
#   can't use right = midIdx - 1 bc of two cases where middle smaller than rightIdx

# Casey's solution:
#     if nums[midIdx] > nums[rightIdx]:
#         leftIdx = midIdx + 1
#     else:
#         rightIdx = midIdx
# explanation: bc of division floor, use greater than comparison instead of less than
# so don't have to worry that leftIdx is the smallest        
