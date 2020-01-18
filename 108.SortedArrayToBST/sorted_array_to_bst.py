# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return 
        low, high = 0, len(nums) -1
        
        return self.create(nums,low,high)
        
    def create(self,arr,low,high):
        if low > high:
            return None
        mid = low + (high - low) //2
        
        newNode = TreeNode(arr[mid])
        
        newNode.left = self.create(arr,low,mid-1)
        newNode.right = self.create(arr,mid+1,high)
        return newNodes