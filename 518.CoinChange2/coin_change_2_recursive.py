class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.recursive(coins, amount, len(coins))
    
    def recursive(self, coins, amount, idx):
        if amount == 0:
            return 1
        if idx <= 0:
            return 0
        
        
        if coins[idx - 1] <= amount:
            return self.recursive(coins, amount-coins[idx-1], idx) + self.recursive(coins, amount, idx-1)
        else:
            return self.recursive(coins, amount, idx-1)