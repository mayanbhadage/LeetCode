class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        
        #sorted_intervals = sorted(intervals, key = lambda x:x[0])
        intervals.sort()
        stack = [intervals[0]]
        
        for i in range(1, len(intervals)):
            a = stack[-1]
            b = intervals[i]
            
            if b[0] >= a[1]:
                stack.append(b)
            else:
                return False
        return True