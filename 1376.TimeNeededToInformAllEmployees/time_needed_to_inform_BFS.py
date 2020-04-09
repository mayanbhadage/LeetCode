class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        hmap = collections.defaultdict(list)
        
        for idx, man in enumerate(manager):
            hmap[man].append(idx)
            
        queue = deque()
        queue.append((headID, informTime[headID]))
        
        result = []
        while queue:
            curr_level = []
            num_emp = len(queue)
            
            for _ in range(num_emp):
                currEmp, currTime = queue.popleft()
                
                if currEmp in hmap:
                    for sub in hmap[currEmp]:
                        queue.append((sub, currTime + informTime[sub]))
                
                else:
                    result.append(currTime)
        return max(result)