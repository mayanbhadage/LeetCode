class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        min_heap = []
        intervals.sort() #Sort by start time
        
        for interval in intervals:
            if min_heap and interval[0] >= min_heap[0]: #This means we can reuse the same room 
                # as the earliest ending time is less than the start of new meeting
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
        return len(min_heap)