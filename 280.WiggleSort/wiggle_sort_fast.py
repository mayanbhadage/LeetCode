class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        less = True
        
        i = 0
        while (i < len(nums) - 1):
            if less:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            
            i += 1
            less = not less