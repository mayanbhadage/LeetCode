class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1
        
        while(row < len(matrix) and col >= 0):
            current_value = matrix[row][col]
            
            if current_value == target:
                return True
            elif current_value > target:
                col -= 1
            else:
                row += 1
        return False