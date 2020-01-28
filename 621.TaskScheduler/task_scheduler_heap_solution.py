import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Solution 2 with max heap
    
    # Create frequency counter for the tasks
    
        task_map = {}
        for task in tasks:
            if task in task_map:
                task_map[task] += 1
            else:
                task_map[task] = 1
        curr_heap = []
        curr_time = 0

        # Adding these value to heap
        # -ve value because this is a min heap and we want most frequent item (max) on the top 
        for key, value in task_map.items():
            heapq.heappush(curr_heap,(-value,key))

        
        while curr_heap:
            idx = 0
            temp = []
            
            while(idx <= n):
                curr_time += 1
                
                if curr_heap:
                    freq , key = heapq.heappop(curr_heap)
                    
                    if freq != -1:
                        temp.append((freq+1,key)) # cosider this task done
                        
                if not curr_heap and not temp:
                    break
                    
                else:
                    idx += 1
                
                
            #Now we hve all items in the temp so need to put back these items in the heap
            
            for item in temp:
                heapq.heappush(curr_heap,item)
        return curr_time