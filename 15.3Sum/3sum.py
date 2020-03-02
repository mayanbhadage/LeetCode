class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        
        for i in range(len(nums) ):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            start = i + 1
            end = len(nums) - 1
            
            while(start < end):
                if nums[start]  + nums[end] == target:
                    result.append([nums[i],nums[start],nums[end]])
                    start += 1
                    while(start < end and nums[start] == nums[start - 1]):
                        start += 1
                elif nums[start]  + nums[end] < target:
                    start += 1
                else:
                    end -= 1
                    
        return result