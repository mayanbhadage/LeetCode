class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        h1 = {value:index for index,value in enumerate(arr1)}
        h2 = {value:index for index,value in enumerate(arr2)}
        h3 = {value:index for index,value in enumerate(arr3)}
        
        result = []
        
        for key,value in h1.items():
            if key in h2 and key in h3:
                result.append(key)
                
        return result