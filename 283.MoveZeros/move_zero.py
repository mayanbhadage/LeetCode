class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        size = len(nums)
        i = 0
        while(i < size):
            if nums[i] == 0:
                count +=1
                del nums[i]
                size -= 1
            else:
                i+=1
                
         nums += [0] * count # this is more efficient