class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        while True:
            # 1.Crush
            candy = set()
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if row > 1 and board[row][col]:
                        if board[row][col] == board[row-1][col] == board[row-2][col]:
                            candy |= {(row,col),(row-1,col),(row-2,col)}
                    if col > 1 and board[row][col]:
                        if board[row][col] == board[row][col-1] == board[row][col-2]:
                            candy |= {(row,col),(row,col-1),(row,col-2)}
                            
            # if dont have candies to crush
            if not candy:
                break
                
            #set found sequence to zero
            for value in candy:
                i , j = value
                board[i][j] = 0
            
            #Drop
            #travers bottem left to top right and adjust values
            
            for j in range(len(board[0])):
                idx = len(board) - 1
                for i in reversed(range(len(board))):
                    if board[i][j]:
                        board[idx][j] = board[i][j]
                        idx -= 1
                for i in range(idx+1):
                    board[i][j] = 0
        return board