class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()
        
        i = 0
        n = len(nums)
        
        while(i < n):
            if nums[i] != i + 1: #current number is not on proper positon
                if nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1],nums[i] = nums[i], nums[nums[i] - 1]
                else:
                    result.add(nums[i])
                    i += 1
            else:
                i += 1
        return result