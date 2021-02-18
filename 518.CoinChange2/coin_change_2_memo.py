class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0 and len(coins) == 0:
            return 1
        self.dp = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        # for d in self.dp:
        #     print(d)
        self.recursive(coins, amount, len(coins))
        return self.dp[len(coins)][amount]

    def recursive(self, coins, amount, idx):
        if amount == 0:
            self.dp[idx][amount] = 1
        if idx <= 0:
            self.dp[idx][amount] =  0
        if self.dp[idx][amount] != -1:
            return self.dp[idx][amount]
        
        if coins[idx - 1] <= amount:
            self.dp[idx][amount]= self.recursive(coins, amount-coins[idx-1], idx) + self.recursive(coins, amount, idx-1)
            return self.dp[idx][amount]
        else:
            self.dp[idx][amount] = self.recursive(coins, amount, idx-1)
            return self.dp[idx][amount]