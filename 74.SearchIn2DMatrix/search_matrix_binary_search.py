class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        
        while(row < len(matrix) and col >= 0):
            curr = matrix[row][col]
            
            if curr == target:
                return True
            
            elif curr < target:
                row += 1
            else:
                col -= 1
        return False