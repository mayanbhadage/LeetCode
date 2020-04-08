class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        target_index = 0
        subseq_cnt = 0
        
        while(target_index < len(target)):
            source_index = 0
            subseq_exist = False
            
            while(source_index < len(source) and target_index < len(target)):
                
                if source[source_index] == target[target_index]:
                    source_index += 1
                    target_index += 1
                    subseq_exist = True
                else:
                    source_index += 1
            subseq_cnt += 1
                
            if not subseq_exist:
                return -1
            
        return subseq_cnt