class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        
        for i, num in enumerate(nums):
            n = target - num
            if n in hmap:
                return [hmap[n], i]
            else:
                hmap[num] = i