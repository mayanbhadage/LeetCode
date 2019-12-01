class Solution:
    def __init__ (self):
        self.array = []
    def transformArray(self, arr: List[int]) -> List[int]:
        newarr = []
        newarr.append(arr[0])
        for x in range(1,len(arr)-1):
            if(arr[x] < arr[x-1] and arr[x] < arr[x+1]):
                newarr.append(arr[x] + 1)
            elif (arr[x] > arr[x-1] and arr[x] > arr[x+1]):
                newarr.append(arr[x] -1)
            else:
                newarr.append(arr[x])
            
        newarr.append(arr[len(arr) -1])
       # print(f"arr: {arr}   newarr: {newarr}")
        if newarr != arr:
            result = self.transformArray(newarr)
        else:
            return newarr
    
        return result