class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
    
        #If sum is odd partation into equal sum is not possible (p1 + p2) = sum => if p1 == p2 sum should we          even
        if sum_ % 2 != 0:
            return False
        
        sum_ = sum_//2
        
        self.dp = [[None] * (sum_ + 1) for _ in range(len(nums) + 1)]
        self.subset_sum(nums, sum_, len(nums)) 
        # for i in range(len(self.dp)):
        #     print(self.dp[i])
        return self.dp[len(nums)][sum_]
        
    def subset_sum(self,nums, sum_, n):
        if sum_ == 0:
            return True
        if n == 0:
            return False
        
        if self.dp[n][sum_] != None:
            return self.dp[n][sum_]

        if nums[n - 1] <= sum_:
            #Now we have 2 choices either we consider the currNum or not
            self.dp[n][sum_] = self.subset_sum(nums, sum_ - nums[n- 1], n - 1) or self.subset_sum(nums, sum_, n -1)
            return self.dp[n][sum_]
        else:
            self.dp[n][sum_] = self.subset_sum(nums, sum_, n - 1)
            return self.dp[n][sum_] 