class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #create dict of frequency of task
        hmap = {}
        for task in tasks:
            if task in hmap:
                hmap[task] += 1
            else:
                hmap[task] = 1
                
        #sort the dict in reverse orders of freq
        #Get the num with maz frequenxt
        
        lst = sorted(hmap.values(),reverse = True)
        max_num = lst[0]
        
        # count how many max nums we have:
        count = 0
        for num in lst:
            if num == max_num:
                count += 1
        ret = (max_num - 1) * (n + 1) + count
        
        return max(ret,len(tasks))
        
        
        