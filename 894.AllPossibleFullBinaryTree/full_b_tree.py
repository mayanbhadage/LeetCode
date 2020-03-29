class Solution:
    def __init__(self):
        self.memo = {0:[], 1:[TreeNode(0)]}
        
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in self.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        new = TreeNode(0)
                        new.left = left
                        new.right = right
                        ans.append(new)
            self.memo[N] = ans
        
        return self.memo[N]
