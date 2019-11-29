class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hmap = {}
        for x in nums:
            if x in hmap:
                return True
            else:
                hmap[x] =1
        
        return False