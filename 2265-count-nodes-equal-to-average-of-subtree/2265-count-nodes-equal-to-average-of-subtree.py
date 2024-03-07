# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt=0
        
        def DFS(root):
            nonlocal cnt
            
            if not root:
                return 0,0
            left_sum, left_n = DFS(root.left)
            right_sum, right_n = DFS(root.right)
            
            s=root.val+left_sum+right_sum
            n=1+left_n+right_n
            
            if s//n==root.val:
                cnt+=1
            return s,n
        
        DFS(root)
        return cnt
        
        