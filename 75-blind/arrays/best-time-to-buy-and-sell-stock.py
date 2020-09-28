class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1: return 0
        lowest = prices[0]
        profit = 0
        for p in prices:
            if p < lowest: 
                lowest = p
            elif p - lowest > profit:
                profit = p - lowest
        return profit
        
        
    # brute force approach
        # n = len(prices)
        # if n == 0 or n == 1: return 0
        # profit = [0]*n
        # for i in range(1,n):
        #     profit[i] = prices[i] - min(prices[:i+1])
        # return max(profit)
