# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt=0
        self.result=None
        self.inorder(root,k)
        return self.result
    
    def inorder(self, root, k):
        if root==None:
            return
        self.inorder(root.left,k)
        self.cnt+=1
        if self.cnt==k:
            self.result=root.val
            return
        self.inorder(root.right,k)