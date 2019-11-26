class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        result = []
        for i in nums1:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        for j in nums2:
            if j in hmap: 
                result.append(j)
        
        return (list(set(result)))