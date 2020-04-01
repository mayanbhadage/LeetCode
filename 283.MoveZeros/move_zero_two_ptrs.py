class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ptr1 = 0
        ptr2 = 0
        
        while(ptr1 < len(nums)-1):
            if nums[ptr1] == 0:
                if ptr2 < ptr1:
                    ptr2 = ptr1
                #find the next non zero
                while(ptr2<len(nums)-1):
                    if nums[ptr2] != 0:
                        break
                    ptr2 += 1
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            ptr1+=1
            
            
        