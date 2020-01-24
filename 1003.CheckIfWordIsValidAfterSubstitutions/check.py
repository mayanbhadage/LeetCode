class Solution:
    def isValid(self, S: str) -> bool:
        if S[0] != 'a' or S[-1] != 'c':
            return False
        hmap = {}
        
        for i in range(1,len(S)):
            if S[i-1] == 'b' and S[i] == 'b':
                return False
            if S[i-1] == 'a' and S[i] =='c':
                return False
            if S[i-1] in hmap:
                hmap[S[i-1]] += 1
            else:
                hmap[S[i-1]] = 1
        if S[-1] in hmap:
            hmap[S[-1]] += 1
        else:
            hmap[S[-1]] = 1
        
        if hmap['a'] != hmap['b'] or hmap['b'] != hmap['c'] or hmap['c'] != hmap['a']:
            return False
        else:
            return True
        