class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        #get the frequency of words:
        
        word_freqs = sorted([self.frequency(word) for word in words])
        
        result = []
        #Now for each query:
        # 1. calculate its freq
        for q in queries:
            # 1. calculate freq of smallest char 
            cnt = self.frequency(q)
            
            #we perform binary search to find the last index
            #cnt is smaller
            
            idx = bisect.bisect_right(word_freqs, cnt)
            result.append(len(words)-idx)
        return result
            
        
        
    def frequency(self,string):
        counter = [0] * 26
        
        for ch in string:
            idx = ord(ch) - ord('a')
            counter[idx] += 1
        
        for cnt in counter:
            if cnt != 0:
                return cnt
        return -1