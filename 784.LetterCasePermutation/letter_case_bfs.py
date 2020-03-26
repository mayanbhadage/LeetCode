class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        length = len(S)
        perm = deque()
        perm.append([])
        result = []
        for curr_letter in S:
            
            n = len(perm)
            for _ in range(n):
                old_perm = perm.popleft()
                
                if curr_letter.isalpha():
                    if curr_letter.islower():
                        new_perm1 = list(old_perm)
                        new_perm1.append(curr_letter.upper())
                        if len(new_perm1) == length:
                            result.append(new_perm1)
                        else:
                            perm.append(new_perm1)
                    else:
                        new_perm1 = list(old_perm)
                        new_perm1.append(curr_letter.lower())
                        if len(new_perm1) == length:
                            result.append(new_perm1)
                        else:
                            perm.append(new_perm1)
                new_perm = list(old_perm)
                new_perm.append(curr_letter)
                if len(new_perm) == length:
                    result.append(new_perm)
                else:
                    perm.append(new_perm)
                        
        final = []  
        for arr in result:
            str_ = ""
            for ch in arr:
                str_ += ch
            
            final.append(str_)
        return final
            
                    
               