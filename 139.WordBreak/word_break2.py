class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = set()
        queue = deque([s])
        
        
        while queue:
            curr_word = queue.popleft()
            
            for word in wordDict:
                if curr_word[:len(word)] == word:
                    new_word = curr_word[len(word):]
                    if new_word == "":
                        return True
                
                    if new_word not in seen:
                        queue.append(new_word)
                        seen.add(new_word)
        return False