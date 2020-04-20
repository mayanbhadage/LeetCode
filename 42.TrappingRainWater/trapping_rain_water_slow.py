class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        
        for i in range(1,len(height)):
            left_max = max(height[j] for j in range(0,i+1 ))
            right_max = max(height[j] for j in range(i,len(height)))
            
            trapped_water = min(left_max, right_max) - height[i]
            
            total_water += trapped_water
        return total_water
            
# Time O(n^2)