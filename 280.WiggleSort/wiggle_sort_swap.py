class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
        ptr1 = 1
        ptr2 = ptr1 + 1
        
        while(ptr2 <= len(nums)-1):
            nums[ptr1],nums[ptr2] = nums[ptr2], nums[ptr1]
            
            ptr1 += 2
            ptr2 = ptr1 + 1
        