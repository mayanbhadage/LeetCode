class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Divide and Conquer
        max_sum = self.maximum_subarray(nums, 0, len(nums)-1)
        return max_sum
        
    def maximum_subarray(self,nums, left, right):
        if left == right:
            return nums[right]
        
        mid = (left + right)//2
        
        left_sum = self.maximum_subarray(nums, left, mid)
        right_sum = self.maximum_subarray(nums, mid+1,right)
        crossing_sum = self.crossing_sum(nums, left, right, mid)
        return max(left_sum, right_sum, crossing_sum)
    
    def crossing_sum(self,nums, left, right, mid):
        if left == right:
            return nums[left]
        lm = -math.inf
        ls = 0
        for i in range(mid, left-1, -1):
            ls += nums[i]
            lm = max(ls, lm)
        rs = 0
        rm = -math.inf
        for i in range(mid+1, right+1):
            rs += nums[i]
            rm = max(rs, rm)
        return  lm + rm