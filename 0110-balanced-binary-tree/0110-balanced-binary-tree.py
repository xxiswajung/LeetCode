# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: [TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) +1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        if abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False