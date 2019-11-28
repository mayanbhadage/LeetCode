class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for list_ in A:
            res = []
            list_ = list_[::-1]
            for value in list_:
                if value is 0:
                    res.append(1)
                else:
                    res.append(0)
            result.append(res)
        return result