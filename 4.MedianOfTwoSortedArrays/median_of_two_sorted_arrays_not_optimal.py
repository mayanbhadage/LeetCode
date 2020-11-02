class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        merged = []
        idx1 = 0
        idx2 = 0
        
        while(idx1 < n and idx2 < m):
            if nums1[idx1] < nums2[idx2]:
                merged.append(nums1[idx1])
                idx1 += 1
            else:
                merged.append(nums2[idx2])
                idx2 += 1
        
        if idx1 < n:
            merged.extend(nums1[idx1:])
        if idx2 < m:
            merged.extend(nums2[idx2:])
        print(merged)
        mid  = (m + n)//2
        if (m + n) % 2 == 0:
            return (merged[mid-1] + merged[mid])/2
        else:
            return merged[mid]