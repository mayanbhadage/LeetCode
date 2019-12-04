class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hmap = {}
        result = []
        for x in items:
            #print(f"{x[0]} : {x[1]}")
                if x[0] not in hmap:
                    hmap[x[0]] = [x[1]]
                else:
                    hmap[x[0]].append(x[1])
        
        for key,value in hmap.items():
            res = []
            value.sort(reverse = True)
            while(len(value)>5):
                value.pop()
            hmap[key] = self.getAvg(sum(value),5)
            res.append(key)
            res.append(hmap[key])
            result.append(res)
        
        return (result)
        
    def getAvg(self,total,num):
        
        avg = int(total/num)
        return avg