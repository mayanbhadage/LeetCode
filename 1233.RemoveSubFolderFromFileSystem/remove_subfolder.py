class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        temp = [False] * len(folder)
        folder.sort()
        i = 0;
        j = 1
        while(j < len(folder)):
            t = folder[i] + "/"
            if t in folder[j]:
                temp[j] = True
                j+=1
            else:
                i = j
                j+=1
        result = []
        
        for i in range(len(temp)):
            if temp[i] == False:
                result.append(folder[i])
        return result