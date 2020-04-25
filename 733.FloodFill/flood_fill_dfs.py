class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        if rows == 0 or cols == 0:
            return [[]]
        seen = set()
        curr_color = image[sr][sc]
        for row in range(rows):
            for col in range(cols):
                if row == sr and col == sc:
                    seen.add((row,col))
                    image[row][col] = newColor
                    self.dfs(row, col, image, newColor, curr_color, seen)
        return image
                    
    def dfs(self,currRow, currCol, image, newColor, curr_color, seen):
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        for direction in directions:
            newRow = currRow + direction[0]
            newCol = currCol + direction[1]
            
            if 0 <= newRow < len(image) and 0 <= newCol < len(image[0]):
                if image[newRow][newCol] == curr_color and (newRow,newCol) not in seen:
                    image[newRow][newCol] = newColor
                    seen.add((newRow, newCol))
                    self.dfs(newRow, newCol, image, newColor, curr_color,seen)