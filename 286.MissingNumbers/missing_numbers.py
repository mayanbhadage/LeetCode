class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1] * (len(nums) + 1)
        
        for i in range(len(nums)):
            curr_num = nums[i]
            
            arr[curr_num] = curr_num
            
        for j in range(len(arr)):
            if arr[j] == -1:
                return j