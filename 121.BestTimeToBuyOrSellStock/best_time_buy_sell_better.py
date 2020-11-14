class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
            
        n = len(prices)
        
        max_prices = [0] * n
        min_prices = [0] * n
        
        #filling the max and min array
        
        min_prices[0] = prices[0]
        max_prices[-1] = prices[-1]
        
        for i in range(1, n):
            min_prices[i] = min(min_prices[i-1], prices[i])
        
        for j in range(n-2, -1, -1):
            max_prices[j] = max(max_prices[j + 1], prices[j])
        
        result = 0
        
        for i in range(n):
            result = max(result, max_prices[i] - min_prices[i])
            
        return result