class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        if len(nums) == 4 and len(set(nums)) == 1 and sum(nums) == target: #e.g. [0,0,0,0] & 0
            return [[nums[0] for i in range(4)]]
        
        
        nums.sort()
        
        for m in range(len(nums)-3):
            if m > 0 and nums[m] == nums[m-1]:
                continue
            target1 = target - nums[m]
            for x in range(m+1,len(nums)-2):
                if nums[x] == nums[x-1] :
                    continue
                target2 = target1 - nums[x]
                start = x+1
                end = len(nums) -1
                
                while start < end:
                    currSum =  nums[start] + nums[end]
                    if currSum == target2:
                        result.append((nums[m],nums[x],nums[start],nums[end]))
                        
                        while(start < end and nums[start] == nums[start + 1]):
                            start += 1
                        while(start < end and nums[end] == nums[end-1]):
                            end -= 1
                        start += 1
                        end -= 1
                    elif currSum < target2:
                        start += 1
                    else:
                        end -= 1
        return result