# time O(n), space O(1) bc instead of another array, use variable to keep track of right running product
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        products = [0]*n
        products[0] = nums[0]
        for i in range(1,n):
            products[i] = products[i-1] * nums[i]
            
        reverse = 1
        for i in range(n-1,0,-1):
            products[i] = products[i-1] * reverse
            reverse *= nums[i]
        products[0] = reverse
        return products
        
        
        
# time O(n), space O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        products = [0]*n
        forward = [0]*n
        reverse = [0]*n
        
        forward[0] = nums[0]
        reverse[-1] = nums[-1]
        for i in range(1,n):
            forward[i] = forward[i-1] * nums[i]
            reverse[n-i-1] = reverse[n-i] * nums[n-i-1]
        
        products[0] = reverse[1]
        products[-1] = forward[-2]
        for i in range(1,n-1):
            products[i] = forward[i-1] * reverse[i+1]
        return products
