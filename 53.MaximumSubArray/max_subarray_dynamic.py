class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        #BaseCase
        dp[0] = nums[0]
        
        #Now we traverse from 1 to len(nums)
        #At every point we have two choice, 1. To add the curr num to sum or 2.To start a new subarray
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)