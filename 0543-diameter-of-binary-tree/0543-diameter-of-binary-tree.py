# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def DFS(root):
            if not root:
                return 0
            
            lf=DFS(root.left)
            rg=DFS(root.right)
            self.maxx=max(self.maxx,lf+rg) #caculate total max diameter, used for final answer
            return max(lf,rg) +1 #caulate only for this node's diameter, return the value of "DFS"
        
        self.maxx=0
        DFS(root)
        return self.maxx