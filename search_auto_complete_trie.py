class TrieNode:
    def __init__(self):
        self.isWord = False
        self.childrens = {}
        self.hot_degree = 0



class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        # 1. The first task is to create a trie structure from the sentences
        self.root = TrieNode()
        self.searchTerm = ""
        
        for index, sentence in enumerate(sentences):
            self.builtTrie(sentence, times[index])
        
    def builtTrie(self, sentence, hot):
        node = self.root
        
        for char in sentence:
            if char not in node.childrens:
                node.childrens[char] = TrieNode()
            node = node.childrens[char]
        
        node.isWord = True
        
        node.hot_degree -= hot
        
    
    
    def search(self):
        node = self.root
        res = []
        path = ""
        
        for c in self.searchTerm:
            if c not in node.childrens:
                return res
            path += c
            node = node.childrens[c]
            
        self.dfs(node, path, res)
        
        return [item[1] for item in sorted(res)[:3]]
        
    def dfs(self, node, path, res):
        if node.isWord:
            res.append((node.hot_degree, path))
        
        for c in node.childrens:
            self.dfs(node.childrens[c], path+c, res)

    def input(self, c: str) -> List[str]:
        
        if c != '#':
            self.searchTerm += c
            return self.search()
        else:
            self.builtTrie(self.searchTerm, 1)
            self.searchTerm = ""
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)