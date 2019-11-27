class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = 0
        hmap={}
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
            size +=1
        
        for key,value in hmap.items():
            if value > size/2:
                return key
            