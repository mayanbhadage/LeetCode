class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        
        #If sum is odd partation into equal sum is not possible (p1 + p2) = sum => if p1 == p2 sum should we          even
        if sum_ % 2 != 0:
            return False
        return self.subset_sum(nums, sum_//2, len(nums)) 
        
    def subset_sum(self,nums, sum_, n):
        if sum_ == 0:
            return True
        if n == 0:
            return False

        if nums[n - 1] <= sum_:
            #Now we have 2 choices either we consider the currNum or not
            return self.subset_sum(nums, sum_ - nums[n- 1], n - 1) or self.subset_sum(nums, sum_, n - 1) 
        else:
            return self.subset_sum(nums, sum_, n - 1) 