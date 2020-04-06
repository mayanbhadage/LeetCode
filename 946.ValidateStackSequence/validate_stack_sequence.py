class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        idx = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while(stack and stack[-1] == popped[idx]):
                stack.pop()
                idx += 1
        return idx == len(popped)
        