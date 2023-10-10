# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None} #make a dictionary to record the node's parent. The root node is parent itself.
        
        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        ancestor = set()
        while p :
            ancestor.add(p)
            p = parent[p] #find p's parent from dictionary
        while q not in ancestor: #repeat it while q finds the ancestors from p's ancestors
            q = parent[q]
        
        return q
        