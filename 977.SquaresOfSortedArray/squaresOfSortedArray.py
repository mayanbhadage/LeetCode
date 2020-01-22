class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        #O(n) logic with the help of two pointers
        ans = collections.deque()
        l, r = 0, len(A) - 1
        
        while(l <= r):
            left = abs(A[l])
            right = abs(A[r])
            
            if left > right:
                ans.appendleft(left * left)
                l += 1
            else:
                ans.appendleft(right * right)
                r-=1
        return ans