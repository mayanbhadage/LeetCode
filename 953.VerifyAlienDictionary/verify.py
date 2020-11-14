class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        
        hmap = {}
        for idx, char in enumerate(order):
            hmap[char] = idx
        
        words = [deque(word) for word in words]
        word_idx = 1
        while(word_idx < len(words)):
            word1 = words[word_idx -1]
            word2 = words[word_idx]
            
            w1 = len(word1)
            w2 = len(word2)
            
            while(word1 and word2):
                ch1 = word1.popleft()
                ch2 = word2.popleft()
                
                ch1_idx = hmap[ch1]
                ch2_idx = hmap[ch2]
                print(ch1, ch1_idx, ch2, ch2_idx)
                
                if ch1_idx < ch2_idx:
                    word1 = []
                    break
                elif ch1_idx == ch2_idx:
                    continue
                else:
                    return False
            if word1:
                return False
            
            word_idx += 1
        return True
                
            