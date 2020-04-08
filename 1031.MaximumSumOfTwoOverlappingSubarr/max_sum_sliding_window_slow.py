class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        #Tuple(sliding_window_sum, start_index, end_index)
        Lsum = []
        
        currL = 0
        
        window_start = 0
        
        for window_end in range(len(A)):
            currL += A[window_end]
            
            if window_end - window_start + 1 == L:
                Lsum.append((currL,window_start, window_end))
                currL -= A[window_start]
                window_start += 1
        
        Msum = []
        currM = 0
        window_start = 0
        
        for window_end in range(len(A)):
            currM += A[window_end]
            
            if window_end - window_start + 1 == M:
                Msum.append((currM, window_start, window_end))
                currM -= A[window_start]
                window_start +=1
                
        print(sorted(Lsum))            
        print(sorted(Msum))         
        
                
        result = 0       
        for t1 in Msum:
            Lt, Ls, Le = t1
            for t2 in Lsum:
                Mt, Ms, Me = t2
                if not self.overlap(Ls, Le, Ms, Me):
                    result = max(result, Lt+Mt)
        return result
                
                  
        
    def overlap(self,Lstart,Lend,Mstart,Mend):
        if Mstart <= Lend and Lstart<=Mend:
            return True
        return False
        
        