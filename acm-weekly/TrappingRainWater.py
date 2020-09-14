class Solution(object):
    def trap(self, height):
        
# efficient solution: sacrifice storage complexity, 
# store mins and maxes in an array  
        totalAmt = 0
        
        n = len(height)
        
        if n == 0:
            return 0
        
        left = [0]*n
        right = [0]*n
        
        for j in range(0, n):
            left[j] = max(left[j-1], height[j])
        
        right[n-1] = height[n-1] # base case
        for j in range(n-2, -1, -1): # stop at -1 (lower bound 0), go backward
            right[j] = max(right[j+1], height[j])
        
        for i in range(n):
            totalAmt += min(left[i], right[i]) - height[i]
        
        return totalAmt

# brute force solution O(n^2):
#
#         totalAmt = 0
        
#         for i in range(1, len(height) - 1): # can't store at left/rightmost
#             left = height[i]
#             right = height[i]
            
#             for j in range(0, i + 1):
#                 left = max(left, height[j])
                
#             for j in range(i, len(height)):
#                 right = max(right, height[j])
                
#             totalAmt += min(left, right) - height[i]
        
#         return totalAmt
