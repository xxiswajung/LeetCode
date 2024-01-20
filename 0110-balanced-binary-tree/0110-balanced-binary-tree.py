# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l, r = self.checkHeight(root.left), self.checkHeight(root.right)
        if abs(l-r)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
    
    def checkHeight(self,root):
        if root is None:
            return 0
        return max(self.checkHeight(root.left),self.checkHeight(root.right))+1
        
        
    