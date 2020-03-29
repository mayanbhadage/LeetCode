class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = deque()
        
        #sort the deck
        deck.sort()
        # add the biggest card to our result
        result.append(deck.pop())
        
        while deck: # while deck we rotate our result and add the next biggest number to our deck
            
            result.appendleft(result.pop())
            result.appendleft(deck.pop())
            
        return result