class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for i in range(len(S)):
        
            if S[i] == 'c':
                if not stack or stack.pop() != 'b': # if stack is empty or prev in not b
                    return False
                if not stack or stack.pop() != 'a': # if stack is empty or prev in not b
                    return False
            else:
                stack.append(S[i])
            
        return len(stack) == 0
        