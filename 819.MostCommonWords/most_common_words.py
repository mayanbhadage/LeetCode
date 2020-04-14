import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = re.findall("\w+", paragraph)
        counter = collections.defaultdict(int)
        for word in words:
            counter[word.lower()] += 1
        
        banned = set(banned)
        
        heap = [(-freq, key) for key, freq in counter.items()]
        heapq.heapify(heap)
        
        while(heap):
            freq, word = heapq.heappop(heap)
            if word in banned:
                continue
            return word
        return ""
        