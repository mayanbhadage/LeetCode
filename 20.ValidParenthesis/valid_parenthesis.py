class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        
        stack = []
        
        for ch in s:
            if ch == '(' or ch == '{' or ch =='[':
                stack.append(ch)
            elif ch == ')' or ch == '}' or ch ==']':
                if len(stack) == 0:
                    return False
                
                if ch == ')' and stack[-1] == '(':
                    stack.pop() 
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        
        
        return True