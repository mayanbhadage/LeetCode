class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            
            mid = (right + left)//2
            
            
            curr_capacity = 0
            num_ships = 1
            
            # Simulate loading in ships
            
            for weight in weights:
                curr_capacity += weight
                
                if curr_capacity > mid: #ship capacity is full
                    curr_capacity = weight
                    num_ships += 1
                    
            if num_ships > D:
                left = mid + 1
            
            else:
                right = mid
        return left