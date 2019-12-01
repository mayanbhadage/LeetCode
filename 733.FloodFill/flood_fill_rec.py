class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        max_col = len(image) -1
        max_row = len(image[0]) -1
        oldColor = image[sr][sc]
        self.fill(image,sr,sc,oldColor,newColor,max_row,max_col)
        return image
        
    def fill(self,image, sr,sc,oldColor, newColor,max_row, max_col):
        
        if((sr<0 or sr > max_col)  ):
            return
        if (sc < 0 or sc > max_row):
            return

        if(image[sr][sc] != oldColor or image[sr][sc] == newColor):
            return
        
        image[sr][sc] = newColor
        #go up

        self.fill(image,sr,sc+1,oldColor,newColor,max_row,max_col)
        #go down

        self.fill(image,sr,sc-1,oldColor,newColor,max_row,max_col)
        #go right

        self.fill(image,sr+1,sc,oldColor,newColor,max_row,max_col)
        #go left
        self.fill(image,sr-1,sc,oldColor,newColor,max_row,max_col)
        
        
            