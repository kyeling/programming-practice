class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        maxArea = float("-inf")
        
        while left < right:
            minHeight = min(height[left], height[right])
            maxArea = max(maxArea, minHeight * (right - left))
            
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return maxArea
        
# brute force: O(n^2) to calculate area of every pair of bars and take max
# using 2 pointers: minHeight = min(height1, height2)
        
