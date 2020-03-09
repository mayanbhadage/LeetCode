class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if len(A) == 0 or len(B) == 0:
            return []
        
        #A.sort(key = lambda x:x[0])
        #B.sort(key = lambda x:x[0])
        #print(A,B)
        result = []
        # two pointer method
        
        ptr1 = 0
        ptr2 = 0
        
        
        while(ptr1 < len(A) or ptr2 < len(B)):
            #NO INTERSECTION
            #print(A[ptr1], B[ptr2])
            
            if A[ptr1][0] <= B[ptr2][0] and A[ptr1][1] < B[ptr2][1] and A[ptr1][1] < B[ptr2][0]:
                if ptr1 + 1 < len(A):
                    ptr1 += 1
                else:
                    break
            elif B[ptr2][0] <= A[ptr1][0] and B[ptr2][1] < A[ptr1][1] and B[ptr2][1] < A[ptr1][0]:
                if ptr2 + 1 < len(B):
                    ptr2 += 1
                else:
                    break
                    
            #INTERSECTION CASES
            
            elif A[ptr1][0] < B[ptr2][0] and A[ptr1][1] <= B[ptr2][1] and B[ptr2][0] <= A[ptr1][1]:
                result.append([max(A[ptr1][0], B[ptr2][0]), min(A[ptr1][1], B[ptr2][1])])
                if ptr1 + 1 < len(A):
                    ptr1 += 1
                else:
                    break
                    
            elif B[ptr2][0] < A[ptr1][0] and B[ptr2][1] < A[ptr1][1] and A[ptr1][0] <= B[ptr2][1]:
                result.append([max(A[ptr1][0], B[ptr2][0]), min(A[ptr1][1], B[ptr2][1])])
                if ptr2 + 1 < len(B):
                    ptr2 += 1
                else:
                    break
                    
            elif A[ptr1][0] <= B[ptr2][0] and B[ptr2][1] < A[ptr1][1]:
                result.append([max(A[ptr1][0], B[ptr2][0]), min(A[ptr1][1], B[ptr2][1])])
                if ptr2 + 1 < len(B):
                    ptr2 += 1
                else:
                    break
            
            elif B[ptr2][0] <= A[ptr1][0] and A[ptr1][1] <= B[ptr2][1]:
                result.append([max(A[ptr1][0], B[ptr2][0]), min(A[ptr1][1], B[ptr2][1])])
                if ptr1 + 1 < len(A):
                    ptr1 += 1
                else:
                    break
                    
        return result
                
            
                
                
                
                