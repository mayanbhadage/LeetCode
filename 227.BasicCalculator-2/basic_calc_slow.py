class Solution:
    def calculate(self, s: str) -> int:

        operations = []
        stack = []
        i = 0
        while(i < len(s)):
            
            if s[i].isdigit():
                num = ""
                idx = i
                while(idx < len(s) and s[idx].isdigit() ):
                    num += s[idx]
                    idx += 1
                operations.append(num)
                i = idx - 1
            elif s[i] != " ":
                operations.append(s[i])
                
            i += 1
            
        if len(operations) == 1:
            return int(operations.pop())
        
        i = 0
        while (i < len(operations)-1):
            if operations[i] == "*":
                num1 = int(stack.pop())
                num2 = int(operations[i+1])
                res = num1 * num2
                i += 1
                stack.append(str(res))
            elif operations[i] == "/":
                num1 = int(stack.pop())
                num2 = int(operations[i+1])
                res = num1//num2
                i+=1
                stack.append(str(res))
                
            
            else:
                stack.append(operations[i])
            i+=1
        if len(operations) > 2 and operations[-2] == "+" or operations[-2] == "-":
            stack.append(operations[-1])
        if len(stack) == 1:
            return int(stack.pop())
        
        result = []
        
        i = 0
        print(stack)
        while(i < len(stack) - 1):
            
            if stack[i] == "+":
                num1 = int(result.pop())
                num2 = int(stack[i+1])
                res = num1 + num2
                i += 1
                result.append(str(res))
            elif stack[i] == "-":
                num1 = int(result.pop())
                num2 = int(stack[i+1])
                res = num1 - num2
                i += 1
                result.append(str(res))
            else:
                result.append(stack[i])
            i+=1
            
        if len(result) == 1:
            return int(result.pop())