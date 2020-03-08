class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval) 
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        
        
        result = []
        
        result.append(sorted_intervals[0])
        
        for i in range(1,len(sorted_intervals)):
            b = sorted_intervals[i]
            a = result[-1]
            
            if b[0] > a[1]:
                result.append(b)
            else:
                result[-1][1] = max(a[1],b[1])
            
        return result
            
        