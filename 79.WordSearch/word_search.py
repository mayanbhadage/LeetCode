class TrieNode:
    def __init__(self):
        self.isWord = False
        self.childrens= {}

class Solution:
    

    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols  = len(board), len(board[0])
        result = []
        self.found = False
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    temp = board[row][col]
                    board[row][col] = "#"
                    result .append(self.dfs(row, col, board, word, directions, 1))
                    board[row][col] = temp
        
        
        return self.found
        
    def dfs(self, currRow, currCol, board, word, directions, curr_index):
        if not self.found:
            if curr_index == len(word):
                self.found = True
                return
            for d in directions:
                newRow, newCol  = currRow + d[0], currCol + d[1]
                if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]):
                    if board[newRow][newCol] != "#" and board[newRow][newCol] == word[curr_index]:
                        temp = board[newRow][newCol]
                        board[newRow][newCol] = "#"
                        self.dfs(newRow, newCol, board, word, directions, curr_index + 1)
                        board[newRow][newCol] = temp