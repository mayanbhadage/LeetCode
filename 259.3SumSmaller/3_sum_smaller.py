class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            
            while(start < end):
                if nums[i] + nums[start] + nums[end] < target:
                    count += end - start
                    start += 1
                    
                else:
                    end -= 1
                    
        return count