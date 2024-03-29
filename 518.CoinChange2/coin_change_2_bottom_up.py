class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        
        for c in range(len(dp[0])):
            dp[0][c] = 0
        
        for r in range(len(dp)):
            dp[r][0] = 1
            
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                
                if coins[i-1] <= j:
                    dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(coins)][amount]