class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = "#"
        
        start = 0
        end = len(letters) - 1
        
        while( start <= end):
            mid = start + (end - start) // 2
            
            if letters[mid] == target:
                result = letters[mid + 1] if mid < len(letters) - 1 else letters[0]
                start = mid + 1
            elif letters[mid] < target:
                start = mid + 1
            else:
                result = letters[mid]
                end = mid  - 1
        return result if result != "#" else letters[0]