class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        #DFS from all boundries
        
        rows = len(board)
        if not rows: return
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1:
                    if board[row][col] == "O":
                        board[row][col] = "#"
                        self.dfs(row, col, board)
                if col == 0 or col == cols - 1:
                    if board[row][col] == "O":
                        board[row][col] = "#"
                        self.dfs(row, col, board)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "#":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        
        
    def dfs(self, currRow, currCol, board):
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for d in direction:
            newRow = currRow + d[0]
            newCol = currCol + d[1]
            
            if 0<= newRow < len(board) and 0 <= newCol <len(board[0]):
                if board[newRow][newCol] == "O":
                    board[newRow][newCol] = "#"
                    self.dfs(newRow, newCol, board)
                    
                    