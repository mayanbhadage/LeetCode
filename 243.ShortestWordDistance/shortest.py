class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        indices1= []
        indices2= []
        for i, x in enumerate(words):
            if x == word1:
                indices1.append(i)
            elif(x == word2):
                indices2.append(i)
            else:
                continue
        
        
        min_ = 9999999
        
        for i in indices1:
            for j in indices2:
                x = abs(i - j)
                if(x < min_):
                    min_ = x
        return min_