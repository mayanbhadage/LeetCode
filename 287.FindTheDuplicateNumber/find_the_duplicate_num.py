class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        while( i < n ):
            
            if nums[i] != i + 1: # this means incorrect pos
                if nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1] , nums[i] = nums[i], nums[nums[i] - 1] 
                else:
                    return nums[i]
            else:
                i += 1
        return -1