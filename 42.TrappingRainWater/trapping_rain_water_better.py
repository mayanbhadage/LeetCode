class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # Pre Computing Left max and Right max array
        
        left_max = [height[0]]
        for i in range(1, len(height)):
            left_max.append(max(height[i], left_max[i-1]))
        
        
        right_max = [-1] * len(height)
        right_max[len(height) - 1] = height[-1]
        
        
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
    
       # Calculate trapped water
        total_water = 0
        
        for i in range(1,len(height)):
            trapped_water = min(left_max[i], right_max[i]) - height[i]
            
            total_water += trapped_water
        return total_water
    # Time O(N)
    #Space O(N)
            