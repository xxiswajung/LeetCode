# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        ans = []
        Q=[root]
        
        while Q:
            children = []
            tmp = []
            while Q:
                item=Q.pop(0)
                tmp.append(item.val)
                if item.left:
                    children.append(item.left)
                if item.right:
                    children.append(item.right)
            Q=children
            ans.append(tmp)
        return ans

                    