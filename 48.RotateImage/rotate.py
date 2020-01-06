class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix) != len(matrix[0]):
            return
        
        n = len(matrix)
        
        for i in range(0,int(n/2)):
            first = i
            last = n - 1 - i
            
            for j in range(first,last):
                offset = j - first
                #store top in temp variable
                top = matrix[first][j]
                
                #top = left
                
                matrix[first][j] = matrix[last-offset][first]
                
                #left = bottom
                
                matrix[last-offset][first] = matrix[last][last-offset]
                
                
                #bottom = right
                
                matrix[last][last-offset] = matrix[j][last]
                
                # right = top
                matrix[j][last] = top