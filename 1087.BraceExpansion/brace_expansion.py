class Solution:
    def expand(self, S: str) -> List[str]:
        
        
        length = 0
        for ch in S:
            if ch.isalnum():
                length += 1
        
        inside = False
        result = []
        
        self.bfs(S, 0, len(S), "", result, inside)
    
        return sorted(result)
    
    
    def bfs(self,S,idx, length, currString, result, inside):
        if idx  == length:
            result.append(currString)
            return
        
        if not S[idx].isalnum():
            if S[idx] == "{":
                inside = True
            elif S[idx] == "}":
                inside = False
            self.bfs(S, idx + 1, length, currString, result, inside)
        else:
            if inside:
               #Find all the elements inside
                temp = []
                i = idx
                while S[i] != "}":
                    if S[i].isalnum():
                        temp.append(i)
                    i+= 1
                print(temp)
                for x in temp:
                    self.bfs(S, i+1 , length, currString + S[x], result, False)
                idx = i
            else:
                self.bfs(S, idx + 1, length , currString + S[idx], result, inside)
                
            
            