class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        self.dp = [-1] * len(nums)
        result = self.recursive(nums, len(nums) -1)
        return result
    def recursive(self,nums, idx):
        if idx < 0:
            return 0
        if self.dp[idx] != -1:
            return self.dp[idx]
        self.dp[idx] =  max(nums[idx] + self.recursive(nums, idx - 2), self.recursive(nums, idx - 1))
        return self.dp[idx]
    
        
        