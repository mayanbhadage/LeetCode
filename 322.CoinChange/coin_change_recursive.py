class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #Unbounded Knapsack
        
        #Recursion
        
        result =  self.recursive(coins, amount, len(coins))
        if result == math.inf:
            return -1
        else:
            return result
    def recursive(self,coins, amount, idx):
        if amount == 0:
            return 0
        if idx < 0:
            return math.inf
        
        if coins[idx - 1] <= amount:
            return min(1 + self.recursive(coins, amount - coins[idx -1 ], idx), self.recursive(coins, amount,idx-1))
        else:
            return self.recursive(coins, amount, idx-1)