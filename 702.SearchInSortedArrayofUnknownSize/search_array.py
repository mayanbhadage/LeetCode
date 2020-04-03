# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # Get boundries
        
        low = 0
        high = 1
        
        while (reader.get(high) < target):
            low = high
            high = high * 2
            
        
        # perform binary search
        while( low <= high):
            mid = low + (high - low)//2
            
            temp = reader.get(mid)
            if temp == target:
                return mid
            
            if temp > target:
                high = mid - 1
                
            else:
                low = mid + 1
                
        return -1
        
        