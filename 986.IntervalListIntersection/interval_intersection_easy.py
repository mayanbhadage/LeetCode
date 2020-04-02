class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ptr1 = 0
        ptr2 = 0
        start,end = 0,1
        result = []
        while(ptr1 < len(A) and ptr2 < len(B)):
            
            if A[ptr1][start] <= B[ptr2][end] and B[ptr2][start] <= A[ptr1][end]:
                result.append((max(A[ptr1][start],B[ptr2][start]),min(A[ptr1][end],B[ptr2][end])))
            
            if A[ptr1][end] < B[ptr2][end]:
                ptr1 += 1
            else:
                ptr2+=1
        return result