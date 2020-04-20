class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        char_set = set([c for word in wordList  for c in word])
        wordList = set(wordList)
        queue = deque([(beginWord, 1)])
        found = False
        while(queue):
            num_neighbours = len(queue)
            for _ in range(num_neighbours):
                curr_word , curr_count = queue.popleft()
                if curr_word == endWord:
                    return curr_count
                
                for i in range(len(curr_word)):
                    rv = self.find_match(curr_word, wordList, i, char_set)
                    for value in rv:
                        queue.append((value, curr_count+ 1))
        return 0
        
        
    def find_match(self, word, wordList, idx, char_set):
        result = []
        for c in char_set:
            new_word = (word[:idx] + c + word[idx+1:])
            if new_word in wordList:
                result.append(new_word)
                wordList.remove(new_word)
        return result