class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        hmap_queries = {}
        hmap_words = {}
        
        for query in queries:
            hmap_queries[query] = self.frequency(query)
        
        for word in words:
            hmap_words [word] = self.frequency(word)
        
        res = []
        
        for q in queries:
            count = 0
            for word in words:
                if hmap_queries[q] < hmap_words[word]:
                    count += 1
            res.append(count)
        return res
                
        
    
    def frequency(self,string):
        counter = [0] * 26
        
        for ch in string:
            idx = ord(ch) - ord('a')
            counter[idx] += 1
        
        for cnt in counter:
            if cnt != 0:
                return cnt
        return -1