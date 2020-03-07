class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        sorted_intervals = sorted(intervals, key = lambda x : x[0])
        result = []
        
        
        result.append(sorted_intervals[0])
        
        for i in range(1,len(sorted_intervals)):
            a = result[-1]
            b = sorted_intervals[i]
            
            if b[0] > a[1]:
                result.append(b)
            else:
                result[-1][1] = max(a[1],b[1])
        return result