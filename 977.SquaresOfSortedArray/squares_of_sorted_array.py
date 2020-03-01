class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [0] * len(A)
        
        ptr1 = 0
        ptr2 = len(A) - 1
        
        res_ptr = len(A) -1
        
        while(ptr2 >= ptr1):
            num1 = A[ptr1]
            num2 = A[ptr2]
            square_num1 = num1 * num1
            square_num2 = num2 * num2
            
            if square_num1  > square_num2:
                result[res_ptr] = square_num1
                ptr1 += 1
            else:
                result[res_ptr] = square_num2
                ptr2 -= 1
                
            res_ptr -= 1
            
        return result