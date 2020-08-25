class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        if not digits:
            return []
        
        queue = deque([("",0)])
        result = []
        while( queue):
            currWord, idx = queue.popleft()
            
            if idx == len(digits):
                result.append(currWord)
            else:
                for char in hmap[digits[idx]]:
                        newWord = currWord + char
                        queue.append((newWord, idx+1))

                    
                
            
                        
        return result
                
               
                    