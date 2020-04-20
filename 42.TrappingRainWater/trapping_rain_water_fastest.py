class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        ptr1 = 0 
        ptr2 = len(height) - 1
        lmax = height[ptr1]
        rmax = height[ptr2]
        result = 0
        while(ptr1 <= ptr2):
            lmax = max(lmax, height[ptr1])
            rmax = max(rmax, height[ptr2])
            
            if lmax < rmax:
                result += (lmax - height[ptr1])
                ptr1 += 1
            else:
                
                result +=  (rmax- height[ptr2])
                ptr2 -= 1
            
        return result
        