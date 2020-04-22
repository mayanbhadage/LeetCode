class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        #Create a datastructue for manager: employee
        hmap_manager = collections.defaultdict(list)
        for emp, mgr in enumerate(manager):
            hmap_manager[mgr].append(emp)
        
        max_time = 0
        #Now we will solve this problem with bfs
        
        queue = deque([(headID, informTime[headID])])
        
        while queue:
            #print(queue)
            num_emp = len(queue)
            for _ in range(num_emp):
                currEmp , currTime = queue.popleft()
                
                if currEmp not in hmap_manager:
                    max_time = max(max_time, currTime)
                else:
                    for emps in hmap_manager[currEmp]:
                        newTime = currTime + informTime[emps]
                        queue.append((emps,newTime))
        return max_time