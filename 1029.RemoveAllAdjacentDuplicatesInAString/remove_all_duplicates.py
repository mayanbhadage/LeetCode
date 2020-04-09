class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append((char,1))
                
            else:
                #This means same consecutive characters
                count = stack.pop()[1]
                #if we got less than K consecutive increase the count
                if (count + 1) % k:
                    stack.append((char,count + 1))
                    
                    
        return "".join(char * count for char,count in stack)