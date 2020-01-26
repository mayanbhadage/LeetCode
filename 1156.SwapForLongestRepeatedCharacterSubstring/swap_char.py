class Solution:
    def maxRepOpt1(self, text: str) -> int:
        freq = {}
        for ch in text:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        start = 0
        max_val = 0
        
        while(start < len(text)):
            count = 1
            nxt = -1
            
            # If we encounter same characters
            while(start < len(text) - 1 and text[start] == text[start+1]):
                start += 1
                count += 1
            
            #now we dont find same char
            nxt = start + 1
            
            # now we check if we have same char 1 dist apart
            
            if (start < len(text) -2 and text[start] == text[start+2]):
                start += 2
                count += 1
            
            # Find another contigious substring
            while(start < len(text) - 1 and text[start] == text[start+1]):
                start += 1
                count += 1
                
                
            if freq[text[start]] > count:
                count += 1
                
            max_val = max(count,max_val)
            
            start = nxt
            
        return max_val
                