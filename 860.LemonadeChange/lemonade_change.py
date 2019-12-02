class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hmap_change = {5:0,10:0,20:0}
        
        for bill in bills:
            if bill is 5:
                hmap_change[bill] += 1
            elif bill is 10:
                if hmap_change[5] < 1:
                    return False
                else:
                    hmap_change[bill] +=1
                    hmap_change[5] -=1
            elif bill is 20:
                if hmap_change[10] < 1:
                    if(hmap_change[5] < 3):
                        return False
                    else:
                        hmap_change[bill] +=1
                        hmap_change[5] -= 3
                else:
                    if hmap_change[5] < 1:
                        return False
                    else:
                        hmap_change[bill] +=1
                        hmap_change[10] -=1
                        hmap_change[5] -=1
                        
        return True
                        
                    
            