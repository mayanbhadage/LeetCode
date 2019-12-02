class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap_ransom = {}
        hmap_magazine = {}
        
        for c in ransomNote:
            if c in hmap_ransom:
                hmap_ransom[c] += 1
            else:
                hmap_ransom[c] = 1
        for c in magazine:
            if c in hmap_magazine:
                hmap_magazine[c] += 1
            else:
                hmap_magazine[c] = 1
    
        for key , value in hmap_ransom.items():
            if key not in hmap_magazine or hmap_magazine[key] < value:
                return False
        return True