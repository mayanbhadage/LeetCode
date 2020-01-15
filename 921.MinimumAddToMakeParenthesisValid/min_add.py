class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        
        for s in S:
            if s == '(':
                stack.append('(')
            elif s == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(')')
                else:
                    stack.append(')')
        return len(stack)