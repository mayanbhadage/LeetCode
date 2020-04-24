class TrieNode:
    def __init__(self):
        self.isWord = False
        self.childrens = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def builtTrie(self, word):
        node = self.root
        
        for c in word:
            if c not in node.childrens:
                node.childrens[c] = TrieNode()
            node = node.childrens[c]
        
        node.isWord = True
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        node = t.root
        for word in words:
            t.builtTrie(word)
        
        
        res = []
        
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                self.dfs(row, col, board, node, "", res)
        return res
        
    def dfs(self, currRow, currCol, board, node, path, res):
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        if node.isWord:
            res.append(path)
            node.isWord = False
            
        
        if currRow < 0 or currRow >= len(board) or currCol < 0 or currCol >= len(board[0]):
            return
        
        temp = board[currRow][currCol]
        node = node.childrens.get(temp)
        if not node:
            return
        
        board[currRow][currCol] = "#"
        
        for d in directions:
            nr = currRow + d[0]
            nc = currCol + d[1]
            self.dfs(nr, nc, board , node, path+temp , res)
        board[currRow][currCol] = temp