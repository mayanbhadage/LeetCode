from collections import OrderedDict
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        hmap_plate = {}
        count = 0
        for c in licensePlate:
            if c.isalpha():
                x = c.lower()
                if x in hmap_plate:
                    hmap_plate[x] += 1
                else:
                    hmap_plate[x] = 1
                count += 1

        hmap_answer = OrderedDict()
        min_len  = 999999
        for word in words:
            match = 0
            hmap_word = {}
            
            for c in word:
                if c in hmap_word:
                    hmap_word[c] +=1
                else:
                    hmap_word[c] =1
            
            for key, value in hmap_plate.items():
                if key in hmap_word and value <= hmap_word[key]:
                    match+= value
            if match >= count:
                if min_len > len(word):
                    min_len = len(word)
                hmap_answer[word] = len(word)
            
        for key,value in hmap_answer.items():
            if value == min_len:
                return key
            
            
                    
                
