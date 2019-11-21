class Solution:
    def toGoatLatin(self, S: str) -> str:
        #vowels
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        final = ""
        str_list = S.split()
        length = len(str_list)
        for i,word in enumerate(str_list):
            newword = ""
            #VOWEL CASE
            if word[0] in vowels:
                newword = word
                newword += "ma"
                for x in range(0,i+1):
                      newword += "a"
                final+= newword
                if length > 1 and i is not length-1:
                    final+= " "
            else:
                temp = word[1:]
                temp+=word[0]
                temp+="ma"
                newword = temp
                for x in range(0,i+1):
                    newword+= "a"
                final += newword
                if length > 1 and i is not length-1:
                    final+= " "
        return final
                
                
            