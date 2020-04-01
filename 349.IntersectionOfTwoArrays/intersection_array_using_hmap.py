class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #hashmap solution
        result = set()
        hmap = collections.defaultdict(int)
        for num in nums1:
            hmap[num] += 1
            
        for num in nums2:
            if num in hmap:
                result.add(num)
        
        return result