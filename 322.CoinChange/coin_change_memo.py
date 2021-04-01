class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #Unbounded Knapsack
        
        #Recursion
        self.dp = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        self.recursive(coins, amount, len(coins))

        if self.dp[len(coins)][amount] == math.inf:
            return -1
        elif self.dp[len(coins)][amount] == -1:
            return 0
        else:
            return self.dp[len(coins)][amount]
        
        
    def recursive(self,coins, amount, idx):
        if amount == 0:
            return 0
        if idx < 0:
            return math.inf
        
        if self.dp[idx][amount] != -1:
            return self.dp[idx][amount]
        
        if coins[idx - 1] <= amount:
            self.dp[idx][amount] =  min(1 + self.recursive(coins, amount - coins[idx -1 ], idx), self.recursive(coins, amount,idx-1))
            return self.dp[idx][amount]
        else:
            self.dp[idx][amount] =  self.recursive(coins, amount, idx-1)
            return self.dp[idx][amount]