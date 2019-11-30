class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        f_upper = None
        s_upper = None
        try:
            if(word[0].isupper()):
                f_upper = True
            else:
                f_upper = False
            if(word[1].isupper()):
                s_upper = True
            else:
                s_upper = False
        except:
            return True
        
        if not f_upper and s_upper:
            return False
            
            
        for i in range(2,len(word)):
            if f_upper and s_upper:
                if word[i].islower():
                    return False
                else:
                    continue
            elif f_upper and not s_upper:
                if word[i].isupper():
                    return False
                else:
                    continue
            elif not f_upper and not s_upper:
                if word[i].isupper():
                    return False
                else:
                    continue
        return True

        