class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = [[None] * (sum(stones)//2 + 1) for _ in range(len(stones) + 1)]
        
        # initilize
        
        for i in range(len(dp[0])):
            dp[0][i] = False
        
        for i in range(len(dp)):
            dp[i][0] = True
            
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                
                if j >= stones[i - 1]:
                    dp[i][j] = dp[i-1][j - stones[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        nums = dp[len(stones)]
        #print(nums)
        min_weight = math.inf
        
        for idx, num in enumerate(nums):
            if num == True:
                min_weight = min(min_weight, sum(stones) - 2 * idx)
        return min_weight