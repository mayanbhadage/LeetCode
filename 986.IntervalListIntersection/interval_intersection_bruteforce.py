class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if len(A) == 0 or len(B) == 0:
            return []
        
        A.sort(key = lambda x:x[0])
        B.sort(key = lambda x:x[0])
        #print(A,B)
        result = []
        for ptr1 in range(len(A)):
            for ptr2 in range(len(B)):
                if A[ptr1][1] >= B[ptr2][0] and B[ptr2][1] >= A[ptr1][0]:
                    result.append([max(A[ptr1][0],B[ptr2][0]),min(A[ptr1][1],B[ptr2][1])])
                    
        return result