class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        idx1 = len(S) - 1
        idx2 = len(T) - 1
        
        while(idx1 >= 0 or idx2 >= 0):
            
            i1 = self.getNextValidIndex(S,idx1)
            i2 = self.getNextValidIndex(T,idx2)
            
            if i1 < 0 and i2 < 0:
                return True
            
            if i1 < 0 or i2<0:
                return False
            
            if S[i1] != T[i2]:
                return False
            
            idx1 = i1 - 1
            idx2 = i2 - 1
        return True
        
        
    def getNextValidIndex(self,string,index):
        
        back_space_count = 0
        
        while(index >= 0):
            if string[index] == "#":
                back_space_count += 1
            elif back_space_count > 0:
                back_space_count -= 1
            else:
                break
            index -= 1 
        return index