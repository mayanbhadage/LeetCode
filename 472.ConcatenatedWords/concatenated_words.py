class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Create a result dict
        res = []
        
        #Create a temp dict with words
        words_dict = set(words)
        
        #For each word in given words:
            # 1. Remove the currentWord form the temp dict
            # 2. Perform Check
            # 3. If "Check" returns True -> append the word in final answer
            # 4. After repeating the steps for all the words return the final answer
        for word in words:
            words_dict.remove(word)
            if self.check(word, words_dict) is True:
                res.append(word)
            words_dict.add(word)
        return res
    
    
    # So Whats happening in the check
    
     # 1. First we check if the given word in the is still present in our dict or not
        # This check is required because in recursive calls later we're splitting the word in two part
        # The later part can already present in the dictnory and thus satify our condition
        
        # For Example:
        # Consider the case of "catsdogcats":
        #     if in later we split the word in two parts as "catsdog" and "cats" 
        #     now here cats is already present in the dict so thus return true
    
    # 2. We iterate from last to first in the current word and split the words in two parts
         # For the first part we check if it is in the dict and for the second part we make a recursive             call to check
        #   Why me make a recursive call because the splitter word in second part can also be formed with two or more words
        
        # For example : "catsdogcats" -> 1. "catsdog" + "cats" 
        #                             -> 2.  "cats" + "dogcats" this can be furter divided in recursive
        #                                   -> "cats" + "dog" + "cats" all are in temp dict thus True
        #                              
    
    def check(self, word, d):
        if word in d:
            return True
        
        for i in range(len(word),0, -1):
            if word[:i] in d and self.check(word[i:], d):
                return True
        return False
        