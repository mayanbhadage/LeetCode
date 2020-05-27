class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #Right biased binary search
        
        
        idx = self.right_biased(letters, target)
        
        if idx == -1 or len(letters) == idx + 1:
            return letters[0]
        return letters[idx + 1]
        
        
    def right_biased(self,letters, target):
        low = 0
        high = len(letters) - 1
        
        while(low <= high):
            mid = low + (high - low)//2
            
            if letters[mid] == target:
                low = mid + 1
            elif letters[mid] < target:
                low = mid + 1
            elif letters[mid] > target:
                high = mid - 1
        if high < 0 and letters[high] != target:
            return -1
        return high