class Solution:
    def countOfAtoms(self, formula: str) -> str:

        formula = self.calculate(formula)
        
        elem = ""
        found = False
        hmap = {}
        i = 0
        while( i < len(formula)):
            #print(hmap)
            if formula[i].isupper() and found == False:
                elem += formula[i]
                found = True
                if i == len(formula) - 1:
                    if elem in hmap:
                        hmap[elem] += 1
                    else:
                        hmap[elem] = 1
                    
            elif formula[i].islower() and found == True:
                elem += formula[i]
                if i == len(formula) - 1:
                    if elem in hmap:
                        hmap[elem] += 1
                    else:
                        hmap[elem] = 1
            
            elif formula[i].isdigit() and found == True:
                num = ""
                idx = i
                while(idx < len(formula) and formula[idx].isdigit()):
                    num += formula[idx]
                    idx += 1
                
                num = int(num)
                if elem in hmap:
                    hmap[elem] += num
                else:
                    hmap[elem] = num
                elem = ""
                found = False
                i = idx-1
            elif formula[i].isupper() and found == True:
                if elem in hmap:
                    hmap[elem] += 1
                else:
                    hmap[elem] = 1
                elem = ""
                found = False
                i -= 1
            i += 1
        result = ""
        ress = []
        hmap = {k: v for k, v in sorted(hmap.items(), key=lambda item: item[0])}
        
        for key, value in hmap.items():
            if value == 1:
                ress.append(key)
            else:
                ress.append(key+str(value))
        
        return "".join(x for x in ress)
        
        
        
    def calculate(self,formula):

        f = ""
        i = 0
        while( i < len(formula)):
            #print(f)
            if formula[i] == "(":
                formula = f + self.calculate(formula[i+1:])
                f = ""
                i = 0
                continue
            elif formula[i] == ")":
                num = ""
                idx = i + 1
                while(idx < len(formula) and formula[idx].isdigit()):
                    num += formula[idx]
                    idx += 1
                
                if num == "":
                    num = 1
                else:
                    num = int(num)
                
                string = f * num
            
                return string + formula[idx:]
            else:
                f += formula[i]
            i += 1
        return formula

s = Solution()

print(s.countOfAtoms("(((U42Se42Fe10Mc31Rh49Pu49Sb49)49V39Tm50Zr44Og6)33((W2Ga48Tm14Eu46Mt12)23(RuRnMn11)7(Yb15Lu34Ra19CuTb2)47(Md38BhCu48Db15Hf12Ir40)7CdNi21(Db40Zr24Tc27SrBk46Es41DsI37Np9Lu16)46(Zn49Ho19RhClF9Tb30SiCuYb16)15)37(Cr48(Ni31)25(La8Ti17Rn6Ce35)36(Sg42Ts32Ca)37Tl6Nb47Rh32NdGa18Cm10Pt49(Ar37RuSb30Cm32Rf28B39Re7F36In19Zn50)46)38(Rh19Md23No22PoTl35Pd35Hg)41)50"))






